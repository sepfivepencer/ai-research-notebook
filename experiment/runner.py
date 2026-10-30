#!/usr/bin/env python3
"""Frozen-test, bounded-expression pilot. Standard-library only."""
import argparse, ast, datetime, json, operator, os, platform, re, subprocess, time, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parent
MODEL = 'qwen2.5-coder:0.5b'
OPS = {ast.Add:operator.add, ast.Sub:operator.sub, ast.Mult:operator.mul, ast.FloorDiv:operator.floordiv, ast.Mod:operator.mod}
CMPS = {ast.Lt:operator.lt, ast.LtE:operator.le, ast.Gt:operator.gt, ast.GtE:operator.ge, ast.Eq:operator.eq, ast.NotEq:operator.ne}
FUNCS = {'abs':abs, 'min':min, 'max':max}

def evaluate(expr, x):
    if not isinstance(expr, str) or len(expr) > 400: raise ValueError('expression_missing_or_long')
    tree = ast.parse(expr.strip(), mode='eval')
    if sum(1 for _ in ast.walk(tree)) > 100: raise ValueError('expression_too_complex')
    def visit(n, depth=0):
        if depth > 30: raise ValueError('expression_too_deep')
        if isinstance(n, ast.Constant) and type(n.value) is int and abs(n.value) <= 1000: out=n.value
        elif isinstance(n, ast.Name) and n.id == 'x': out=x
        elif isinstance(n, ast.UnaryOp) and isinstance(n.op,(ast.USub,ast.UAdd)):
            a=visit(n.operand,depth+1); out=-a if isinstance(n.op,ast.USub) else a
        elif isinstance(n, ast.BinOp) and type(n.op) in OPS:
            out=OPS[type(n.op)](visit(n.left,depth+1),visit(n.right,depth+1))
        elif isinstance(n, ast.IfExp): out=visit(n.body if visit(n.test,depth+1) else n.orelse,depth+1)
        elif isinstance(n, ast.Compare) and len(n.ops)==1 and type(n.ops[0]) in CMPS:
            out=CMPS[type(n.ops[0])](visit(n.left,depth+1),visit(n.comparators[0],depth+1))
        elif isinstance(n, ast.BoolOp) and isinstance(n.op,(ast.And,ast.Or)):
            vals=[visit(v,depth+1) for v in n.values]; out=all(vals) if isinstance(n.op,ast.And) else any(vals)
        elif isinstance(n, ast.Call) and isinstance(n.func,ast.Name) and n.func.id in FUNCS and not n.keywords and 1<=len(n.args)<=3:
            out=FUNCS[n.func.id](*(visit(v,depth+1) for v in n.args))
        else: raise ValueError('disallowed_ast_'+type(n).__name__)
        if type(out) not in (int,bool) or abs(out)>100000000: raise ValueError('invalid_or_large_result')
        return out
    result=visit(tree.body)
    if type(result) is not int: raise ValueError('result_not_integer')
    return result

def ref(task,x):
    if task=='abs': return -x if x<0 else x
    if task=='sign': return -1 if x<0 else (1 if x>0 else 0)
    if task=='clamp': return 0 if x<0 else (10 if x>10 else x)
    if task=='even': return 1 if x%2==0 else 0
    if task=='floor_even': return x if x%2==0 else x-1
    if task=='three_floor': return x//3
    if task=='odd_double': return x*2 if x%2 else x//2
    if task=='square_cap': return min(x*x,100)
    if task=='distance_five': return min(x%5,(-x)%5)
    if task=='digits': return len(str(abs(x)))
    raise KeyError(task)

def result(expr,x):
    try: return {'value':evaluate(expr,x)}
    except (ValueError, TypeError, ArithmeticError, SyntaxError, RecursionError) as e: return {'error':str(e)[:120]}

def query(prompt, schema):
    payload={'model':MODEL,'prompt':prompt,'stream':False,'format':schema,'options':{'temperature':0,'seed':42,'num_predict':256,'num_ctx':2048},'keep_alive':'5m'}
    req=urllib.request.Request('http://127.0.0.1:11434/api/generate',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
    started=time.time()
    try:
        with urllib.request.urlopen(req,timeout=180) as res: response=json.load(res)
        raw=response.get('response','')
        try: parsed=json.loads(raw)
        except (ValueError,TypeError): parsed=None
        return {'prompt':prompt,'raw':raw,'parsed':parsed,'done_reason':response.get('done_reason'),'eval_count':response.get('eval_count'),'seconds':round(time.time()-started,3)}
    except Exception as e: return {'prompt':prompt,'raw':'','parsed':None,'error':f'{type(e).__name__}: {e}','seconds':round(time.time()-started,3)}

EXPR_SCHEMA={'type':'object','properties':{'expression':{'type':'string'}},'required':['expression']}
TEST_SCHEMA={'type':'object','properties':{'tests':{'type':'array','items':{'type':'object','properties':{'input':{'type':'integer'},'expected':{'type':'integer'}},'required':['input','expected']}}},'required':['tests']}

def checked_tests(data):
    raw=data.get('tests') if isinstance(data,dict) else None
    if not isinstance(raw,list): return [], ['tests_not_array']
    good=[]; rejected=[]
    for t in raw:
        if len(good)>=6: rejected.append('above_6_tests'); continue
        if not isinstance(t,dict) or type(t.get('input')) is not int or type(t.get('expected')) is not int or not -20<=t['input']<=20 or abs(t['expected'])>1000000:
            rejected.append('invalid_test'); continue
        good.append({'input':t['input'],'expected':t['expected']})
    return good,rejected

def selfcheck(expr,tests):
    out=[]
    for t in tests:
        r=result(expr,t['input']); out.append({**t,'actual':r,'pass':r.get('value')==t['expected'] and 'error' not in r})
    return out

def gen(task):
    spec=task['spec']; prefix=f"Task: {spec}\nInput: x is an integer between -20 and 20 inclusive. Return an integer.\n"
    code_prompt=prefix+"Give a single Python expression using x, integer literals, + - * // %, comparisons, conditional expressions and abs/min/max. No function definitions, imports, lists, or explanations. Output JSON with key expression."
    first=query(code_prompt,EXPR_SCHEMA); obj=first.get('parsed'); expr=obj.get('expression','') if isinstance(obj,dict) else ''
    test_prompt=prefix+f"Candidate expression: {expr}\nGenerate 4 to 6 distinct tests of the specification. Return JSON as {{\"tests\":[{{\"input\": integer, \"expected\": integer}}]}}."
    testcall=query(test_prompt,TEST_SCHEMA); tests,rejected=checked_tests(testcall.get('parsed'))
    record={'task':task,'initial_call':first,'test_call':testcall,'tests':tests,'rejected_tests':rejected,'rounds':[]}
    for i in range(3):
        checks=selfcheck(expr,tests); record['rounds'].append({'round':i,'expression':expr,'self_checks':checks})
        if not tests or all(c['pass'] for c in checks) or i==2: break
        failures=[{'input':c['input'],'expected':c['expected'],'actual':c['actual']} for c in checks if not c['pass']]
        prompt=prefix+f"Your current expression is {expr}. It fails these tests: {json.dumps(failures)}. Fix the expression. Return only JSON with key expression. Use the permitted Python expression operators."
        call=query(prompt,EXPR_SCHEMA); record['rounds'][-1]['repair_call']=call
        obj=call.get('parsed'); expr=obj.get('expression','') if isinstance(obj,dict) else ''
    return record

def analyze(path):
    data=json.loads(path.read_text())
    for rec in data['tasks']:
        ident=rec['task']['id']; rec['test_oracle_disagreements']=[t for t in rec['tests'] if ref(ident,t['input'])!=t['expected']]
        for rnd in rec['rounds']:
            failures=[]
            for x in range(-20,21):
                actual=result(rnd['expression'],x); expected=ref(ident,x)
                if actual.get('value')!=expected or 'error' in actual: failures.append({'x':x,'expected':expected,'actual':actual})
            rnd['independent_failure_count']=len(failures); rnd['independent_failures']=failures
            rnd['self_all_pass']=bool(rec['tests']) and all(c['pass'] for c in rnd['self_checks'])
            rnd['independent_all_pass']=not failures
            rnd['false_pass']=rnd['self_all_pass'] and not rnd['independent_all_pass']
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    initial=[r['rounds'][0] for r in data['tasks']]; final=[r['rounds'][-1] for r in data['tasks']]
    summary={'tasks':len(data['tasks']),'completed':data['complete'],'with_usable_tests':sum(bool(r['tests']) for r in data['tasks']),'initial_self_pass':sum(x['self_all_pass'] for x in initial),'final_self_pass':sum(x['self_all_pass'] for x in final),'initial_independent_pass':sum(x['independent_all_pass'] for x in initial),'final_independent_pass':sum(x['independent_all_pass'] for x in final),'initial_false_pass':sum(x['false_pass'] for x in initial),'final_false_pass':sum(x['false_pass'] for x in final),'tasks_with_bad_test_oracles':sum(bool(r['test_oracle_disagreements']) for r in data['tasks']),'repairs':sum(len(r['rounds'])-1 for r in data['tasks'])}
    (path.parent/(path.stem+'-summary.json')).write_text(json.dumps(summary,indent=2)+'\n'); print(json.dumps(summary,indent=2))

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',default=str(ROOT/'runs'/'pilot.json')); p.add_argument('--analyze-only',action='store_true'); args=p.parse_args(); path=Path(args.output)
    if args.analyze_only: analyze(path); return
    tasks=json.loads((ROOT/'tasks.json').read_text()); path.parent.mkdir(parents=True,exist_ok=True)
    modelinfo=subprocess.run(['ollama','show',MODEL,'--modelfile'],capture_output=True,text=True,timeout=30)
    listing=subprocess.run(['ollama','list'],capture_output=True,text=True,timeout=30)
    data={'protocol':'experiment/protocol.md','utc_started':datetime.datetime.now(datetime.timezone.utc).isoformat(),'platform':platform.platform(),'python':platform.python_version(),'model':MODEL,'ollama_version':subprocess.run(['ollama','--version'],capture_output=True,text=True).stdout.strip(),'ollama_list':listing.stdout,'model_modelfile':modelinfo.stdout,'tasks':[],'complete':False}
    for task in tasks:
        print('Running',task['id'],flush=True); data['tasks'].append(gen(task)); path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    data['complete']=True; data['utc_finished']=datetime.datetime.now(datetime.timezone.utc).isoformat(); path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n'); analyze(path)
if __name__=='__main__': main()
