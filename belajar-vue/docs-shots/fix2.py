# -*- coding: utf-8 -*-
"""Perbaikan token & caption tabel pada file sumber laporan."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FIXES = [
    (r"dengan\s+origine\s+yang", "dengan asal yang"),
    (r"pemetaan terhadap capaian pembelajaran disajikan pada Tabel 3\.2",
     "pemetaan terhadap capaian pembelajaran disajikan pada Tabel 3.1"),
    (r'(\["F-13", "Menyimpan data event agar tetap tersedia setelah reload",\s*\n'
     r'\s*"useEvents\.js dengan localStorage"\]\],\s*\n\s*)None,',
     r'\1"Tabel 3.2  Analisis Kebutuhan Fungsional Aplikasi Gatherly",'),
]


def apply(path):
    txt = open(path, encoding="utf-8").read()
    orig = txt
    for pat, rep in FIXES:
        new = re.sub(pat, rep, txt)
        print(("OK   " if new != txt else "MISS ") + pat[:60])
        txt = new
    if txt != orig:
        open(path, "w", encoding="utf-8").write(txt)
        print("  -> ditulis:", path)
    else:
        print("  -> tidak ada perubahan:", path)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print("===", p)
        apply(p)
