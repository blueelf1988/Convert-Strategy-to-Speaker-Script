#!/usr/bin/env python3
"""
Build a professional Word speaker script from structured Markdown.
V2: Supports main-script-first node structure with punchline insights.

Usage:
    python3 build_speaker_docx.py --input speaker-script.md --output speaker-script.docx

Dependencies: python-docx, lxml
"""

import argparse
import re
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn


def main():
    parser = argparse.ArgumentParser(description="Build a speaker script DOCX")
    parser.add_argument("--input", required=True, help="Input Markdown file")
    parser.add_argument("--output", required=True, help="Output DOCX path")
    parser.add_argument("--title", default="现场提案口播稿", help="Cover title")
    parser.add_argument("--subtitle", default="", help="Cover subtitle")
    parser.add_argument("--client", default="", help="Client name")
    parser.add_argument("--agency", default="", help="Agency name")
    parser.add_argument("--duration", default="80-100 分钟", help="Estimated duration")
    args = parser.parse_args()

    doc = Document()

    # Set default font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Microsoft YaHei'
    font.size = Pt(11)
    style.paragraph_format.line_spacing = 1.2

    # Cover page (simplified)
    doc.add_paragraph("")
    doc.add_paragraph("")

    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title_p.add_run(args.title)
    run.bold = True
    run.font.size = Pt(26)

    if args.subtitle:
        sub_p = doc.add_paragraph()
        sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = sub_p.add_run(args.subtitle)
        run.font.size = Pt(16)

    # Read input markdown and convert to paragraphs
    with open(args.input, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Headings
        if line.startswith('# '):
            p = doc.add_heading(line[2:], level=1)
        elif line.startswith('## '):
            p = doc.add_heading(line[3:], level=2)
        elif line.startswith('### '):
            p = doc.add_heading(line[4:], level=3)
        else:
            p = doc.add_paragraph(line)

    doc.save(args.output)
    print(f"DOCX saved to: {args.output}")


if __name__ == "__main__":
    main()
