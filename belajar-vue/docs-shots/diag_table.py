# -*- coding: utf-8 -*-
"""Periksa XML tabel pada dokumen final (setelah disimpan ulang oleh Word)."""
import re
import sys

from docx import Document
from docx.oxml.ns import qn

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOCX = r"C:\Users\HP\Documents\P UI 2\belajar-vue\Laporan_Praktikum_PUI_Lanjut_Modul0-1.docx"

strip = lambda s: re.sub(r'\sxmlns:[a-zA-Z0-9]+="[^"]*"', "", s)

d = Document(DOCX)
for idx in (0, 2, 6, 12):
    t = d.tables[idx]
    print("=" * 70)
    print("TABEL", idx + 1, "-", len(t.rows), "baris x", len(t.columns), "kolom")
    print(strip(t._tbl.tblPr.xml))
    grid = t._tbl.find(qn("w:tblGrid"))
    cols = [c.get(qn("w:w")) for c in grid.findall(qn("w:gridCol"))]
    print("  gridCol:", cols, " total:", sum(int(c) for c in cols))
    print("  tcW   :", [c._tc.tcPr.find(qn("w:tcW")).get(qn("w:w")) for c in t.rows[0].cells])
