# -*- coding: utf-8 -*-
"""Perbaikan final token korup di file sumber laporan."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TARGET = r"C:\Users\HP\Documents\P UI 2\belajar-vue\docs-shots\sections_b.py"

FIXES = [
    (r"loc: eventData\.loc\.startsWith\('\?\?'\) \? eventData\.loc : `\?\? \$\{eventData\.loc\}`,",
     "loc: eventData.loc.startsWith('\U0001F4CD') ? eventData.loc : `\U0001F4CD ${eventData.loc}`,"),
    (r"Komponen ui encapsulate elemen antarmuka generik",
     "Komponen ui mengemas elemen antarmuka generik"),
]

txt = open(TARGET, encoding="utf-8").read()
for pat, rep in FIXES:
    new = re.sub(pat, rep, txt)
    print(("OK   " if new != txt else "MISS ") + pat[:55])
    txt = new
open(TARGET, "w", encoding="utf-8").write(txt)
print("selesai")
