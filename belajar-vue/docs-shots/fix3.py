# -*- coding: utf-8 -*-
"""Perbaikanfinal untuk token korup tersisa di sections_b.py."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PATHS = [
    r"C:\Users\HP\Documents\P UI 2\belajar-vue\docs-shots\sections_b.py",
]

FIXES = [
    (r"Halaman EventDetail merupakan ujung\s+\S+\s+destination dalam ",
     "Halaman EventDetail merupakan ujung destinasi dalam "),
    (r"Sembilan halaman\S* yang berarti ",
     "Sembilan halaman yang masing-masing hanya "),
]

for p in PATHS:
    txt = open(p, encoding="utf-8").read()
    for pat, rep in FIXES:
        new = re.sub(pat, rep, txt)
        print(("OK   " if new != txt else "MISS ") + pat[:55])
        txt = new
    open(p, "w", encoding="utf-8").write(txt)

print("selesai")
