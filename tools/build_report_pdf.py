#!/usr/bin/env python3
"""Build a readable Chinese report PDF from the canonical Markdown; needs reportlab."""
from html import escape
from pathlib import Path
import re
import os
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'paper' / '研究报告.md'
OUTPUT = ROOT / 'output' / 'pdf' / 'ai-self-test-report.pdf'
BLUE = colors.HexColor('#0758bf')
INK = colors.HexColor('#171a20')
font_candidates = [os.environ.get('REPORT_CHINESE_FONT', ''), '/System/Library/Fonts/STHeiti Light.ttc', '/System/Library/Fonts/Supplemental/Arial Unicode.ttf']
font_path = next((p for p in font_candidates if p and Path(p).is_file()), None)
if font_path is None:
    raise SystemExit('Set REPORT_CHINESE_FONT to a Chinese TrueType font path; reportlab is also required.')
pdfmetrics.registerFont(TTFont('ChineseEmbedded', font_path, subfontIndex=0))
body = ParagraphStyle('body', fontName='ChineseEmbedded', fontSize=10.2, leading=17, spaceAfter=8, textColor=INK, wordWrap='CJK')
h1 = ParagraphStyle('title', parent=body, fontSize=23, leading=32, spaceAfter=18, textColor=BLUE, keepWithNext=True)
h2 = ParagraphStyle('section', parent=body, fontSize=15, leading=22, spaceBefore=15, spaceAfter=9, keepWithNext=True)
h3 = ParagraphStyle('subsection', parent=body, fontSize=11.8, leading=19, spaceBefore=10, keepWithNext=True)
cell = ParagraphStyle('cell', parent=body, fontSize=9.2, leading=14, spaceAfter=0)


def inline(text):
    codes = []
    def save_code(match):
        codes.append(match.group(1))
        return 'CODETOKEN' + str(len(codes)-1) + 'END'
    text = re.sub(r'`([^`]+)`', save_code, text)
    links = []
    def save_link(match):
        links.append((match.group(1), match.group(2)))
        return 'LINKTOKEN' + str(len(links)-1) + 'END'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', save_link, text)
    text = escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'\1', text)
    for i, code in enumerate(codes):
        text = text.replace('CODETOKEN'+str(i)+'END', '<font color="#0758bf">'+escape(code)+'</font>')
    for i, (label, url) in enumerate(links):
        if url.startswith('https://'):
            replacement = '<link color="#0758bf" href="'+escape(url,quote=True)+'">'+escape(label)+'</link>'
        else:
            replacement = escape(label)
        text = text.replace('LINKTOKEN'+str(i)+'END', replacement)
    # CID font fallback handles the Chinese text; avoid a few unsupported typographic glyphs.
    return text.replace('²', '的平方').replace('–', '-').replace('—', '-')


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(BLUE)
    canvas.line(46, 40, A4[0]-46, 40)
    canvas.setFont('ChineseEmbedded', 8)
    canvas.setFillColor(colors.HexColor('#666666'))
    canvas.drawString(46, 27, 'AI 自生成测试的本地探索 | 结项报告 2026-11-16')
    canvas.drawRightString(A4[0]-46, 27, str(doc.page))
    canvas.restoreState()


def build():
    lines = SOURCE.read_text().splitlines()
    flow = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                raw = [x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', x) for x in raw):
                    rows.append([Paragraph(inline(x), cell) for x in raw])
                i += 1
            width = A4[0]-92
            widths = [width*0.58] + [width*0.42/(len(rows[0])-1)]*(len(rows[0])-1)
            table = Table(rows, colWidths=widths, repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#edf3fb')),('LINEBELOW',(0,0),(-1,0),0.7,BLUE),('LINEBELOW',(0,1),(-1,-1),0.3,colors.HexColor('#dce0e6')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
            flow.extend([table,Spacer(1,12)])
            continue
        if line.startswith('# '):
            flow.append(Paragraph(inline(line[2:]),h1))
        elif line.startswith('## '):
            flow.append(Paragraph(inline(line[3:]),h2))
        elif line.startswith('### '):
            flow.append(Paragraph(inline(line[4:]),h3))
        else:
            flow.append(Paragraph(inline(line),body))
        i += 1
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=46,leftMargin=46,topMargin=44,bottomMargin=54,title='当自生成测试出错：两次本地代码修复预实验与方法反思',author='sepfivepencer',pageCompression=1)
    doc.build(flow,onFirstPage=footer,onLaterPages=footer)
    print(OUTPUT)

if __name__=='__main__': build()
