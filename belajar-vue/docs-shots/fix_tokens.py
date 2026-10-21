# -*- coding: utf-8 -*-
"""Deteksi dan perbaiki token korup pada file sumber laporan."""
import re
import sys

# karakter CJK / Thai / Devanagari / Cyrillic yang tidak mungkin muncul di teks Indonesia
BAD_CHARS = re.compile(
    r"[\u0400-\u04FF\u0900-\u097F\u0E00-\u0E7F\u3000-\u303F\u3040-\u30FF"
    r"\u4E00-\u9FFF\uF900-\uFAFF\uFF00-\uFFEF]"
)

REPLACEMENTS = [
    (r"Slot adalah mechanism penyisipan", "Slot adalah mekanisme penyisipan"),
    (r"v-model adalah[^\"]*?atas kombinasi props dan emits yang ",
     "v-model adalah jalan pintas atas kombinasi props dan emits yang "),
    (r"mengwikipedia dua arah", "bekerja secara dua arah"),
    (r"dengan origine yang", "dengan asal yang"),
    (r"UjungURANCE destinasi", "Ujung Destinasi"),
    (r"composale diteruskan", "composable diteruskan"),
    (r"Meng enact navigasi", "Mengalihkan navigasi"),
    (r"pada/documentation ", "pada dokumentasi "),
    (r"mulai darioras ", "mulai dari satu "),
    (r"danoutput produksi", "dan keluaran produksi"),
    (r"secara premature", "secara prematur"),
    (r"halamanidipecah", "halaman dipecah"),
    (r"danExecutor ", "sehingga "),
    (r"developershara ", "pengembang "),
    (r"sehingga Umumnya ", "sehingga umumnya "),
    (r"namun kiri bounce ", "namun berpindah "),
    (r"memuat若干 ", "memuat sejumlah "),
    (r"beberapa_library ", "beberapa manfaat penting. Ketiga, "),
    (r"property route\.matched", "properti route.matched"),
    (r"per州の", "per "),
]

TABLE_FIXES = [
    ('"Tabel 3.1  Analisis Kebutuhan Fungsional Aplikasi Gatherly"',
     '"Tabel 3.1  Capaian Pembelajaran Mata Kuliah (CPMK) Modul 0 dan Modul 1"'),
    ('"Tabel 3.2  Kontrak Props dan Emits Antarkomponen"',
     '"Tabel 3.3  Kontrak Props dan Emits Antarkomponen"'),
    ('"Tabel 3.3  Daftar Rute Aplikasi pada src/router/index.js"',
     '"Tabel 3.4  Daftar Rute Aplikasi pada src/router/index.js"'),
    ('"Tabel 3.4  Spesifikasi Teknis Proyek belajar-vue"',
     '"Tabel 3.5  Spesifikasi Teknis Proyek belajar-vue"'),
    ('"Tabel 3.1  Analisis Kebutuhan Fungsional Aplikasi Gatherly",\n        None,',
     '"Tabel 3.2  Analisis Kebutuhan Fungsional Aplikasi Gatherly",'),
    ("dirangkum pada Tabel 3.1, sedangkan", "dirangkum pada Tabel 3.2, sedangkan"),
]


def scan(path):
    txt = open(path, encoding="utf-8").read()
    hits = []
    for i, line in enumerate(txt.split("\n"), 1):
        for m in BAD_CHARS.finditer(line):
            hits.append((i, m.group(), line.strip()[:90]))
    return hits


def fix(path):
    txt = open(path, encoding="utf-8").read()
    orig = txt
    for pat, rep in REPLACEMENTS:
        txt = re.sub(pat, rep, txt)
    for old, new in TABLE_FIXES:
        txt = txt.replace(old, new)
    if txt != orig:
        open(path, "w", encoding="utf-8").write(txt)
    return txt != orig


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    changed = False
    for p in sys.argv[1:]:
        hits = scan(p)
        if hits:
            print("=== CJK/non-latin di %s ===" % p)
            for i, c, line in hits:
                print("  baris %d: %r  -> %s" % (i, c, line))
        if fix(p):
            print("  [fixed] %s" % p)
            changed = True
    if not changed:
        print("tidak ada perubahan")
