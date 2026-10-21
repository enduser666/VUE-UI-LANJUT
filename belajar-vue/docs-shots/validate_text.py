# -*- coding: utf-8 -*-
"""Validasi '&' perbaiki anomali teks pada file sumber laporan."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ALLOWED_NON_ASCII = set("–—’‘“”°×·→…±≤≥µΩéêÉ├─└│─\U0001F4CD\U0001F389\U0001F4A1\U0001F4CC\U0001F6A8\U000026A0")
LATIN_EXTRA = set("áàâäãåéèêëíìîïóòôöõúùûüñçÁÀÂÄÉÈÊËÍÌÎÏÓÒÔÖÚÙÛÜÑÇ")

FIXES = [
    (r"R\.para\(\"localStorage adalah penyimpanan sisi klien dengan[^\w\s]origine yang \"",
     'R.para("localStorage adalah penyimpanan sisi klien yang menyimpan "'),
    (r'"bersifat string\. Pada prototipe aplikasi tanpa server, "',
     '"data dalam bentuk string. Pada prototipe aplikasi tanpa server, "'),
    (r"dirangkum pada Tabel 3\.2 dan Gambar 3\.4",
     "dirangkum pada Tabel 3.3 dan Gambar 3.4"),
    (r"Rangkaian preparatory yang dilakukan praktikan",
     "Rangkaian persiapan yang dilakukan praktikan"),
    (r"Layout publik[^ ]* memuat Navbar di bagian atas dan ",
     "Layout publik memuat Navbar di bagian atas dan "),
    (r"tempat halaman[^ ]* dirender\.", "tempat halaman anak dirender."),
    (r"kontak yang[^ ]* menggunakan event submit\.prevent",
     "kontak yang menggunakan event submit.prevent"),
    (r"Sistem spasi采用的是 kelipatan delapan piksel",
     "Sistem spasi mengadopsi kelipatan delapan piksel"),
    (r"Beberapa temuan值得 dicatat", "Beberapa temuan perlu dicatat"),
    (r"dengan Vitest dan[^ ]* Playwright", "dengan Vitest dan Playwright"),
    (r"merupakan\(Onership\) pergerakan lateral",
     "merupakan pergerakan lateral"),
    (r"Halaman Detail Event merupakan ujung[^ ]* destination",
     "Halaman Detail Event merupakan ujung destinasi"),
    (r"berhasilyelexecute dengan lengkap", "berhasil dieksekusi dengan lengkap"),
    (r"kode yang-ringkas", "kode yang ringkas"),
    (r"Inasersembunyi karena", "Hal ini tersembunyi karena"),
    (r"menestablishedkan arah default", "menetapkan arah default"),
    (r"Halaman EventDetail merupakan ujung [^ ]* destination dalam ",
     "Halaman EventDetail merupakan ujung destinasi dalam "),
    (r"Sembilan halamangowatjubung Lab View yang berarti ",
     "Sembilan halaman、ダイエット yang berarti "),
]


def scan(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    problems = []
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r"[A-Za-z][’'][A-Za-z]", line):
            problems.append((i, "apostrophe-dalam-kata", line.strip()[:100]))
        for ch in line:
            if ord(ch) > 127 and ch not in ALLOWED_NON_ASCII and ch not in LATIN_EXTRA:
                problems.append((i, "karakter-asing: U+%04X %s" % (ord(ch), ch),
                                 line.strip()[:100]))
    return problems


def fix(path):
    txt = open(path, encoding="utf-8").read()
    orig = txt
    for pat, rep in FIXES:
        txt = re.sub(pat, rep, txt)
    if txt != orig:
        open(path, "w", encoding="utf-8").write(txt)
    return txt != orig


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print("===", p)
        probs = scan(p)
        if probs:
            for i, kind, ctx in probs:
                print("  L%-4d %-28s %s" % (i, kind, ctx))
        else:
            print("  bersih")
        if fix(p):
            print("  -> diperbaiki")
