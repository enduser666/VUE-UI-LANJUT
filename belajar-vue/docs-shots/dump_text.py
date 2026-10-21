# -*- coding: utf-8 -*-
"""Cetak seluruh teks naratif dari file sections_*.py untuk proofreading."""
import ast
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FILES = [
    r"C:\Users\HP\Documents\P UI 2\belajar-vue\docs-shots\sections_a.py",
    r"C:\Users\HP\Documents\P UI 2\belajar-vue\docs-shots\sections_b.py",
    r"C:\Users\HP\Documents\P UI 2\belajar-vue\docs-shots\build_report.py",
]

TEXT_FUNCS = {"para", "bullet", "numbered", "h1", "h2", "h3", "code", "figure"}


def lit(node):
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


def collect(fn_node, out):
    for node in ast.walk(fn_node):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            name = node.func.attr
            if name in TEXT_FUNCS and node.args:
                parts = []
                for a in node.args:
                    if isinstance(a, ast.Constant) and isinstance(a.value, str):
                        parts.append(a.value)
                    elif isinstance(a, ast.JoinedStr):
                        parts.append("".join(
                            v.value for v in a.values
                            if isinstance(v, ast.Constant)))
                if parts:
                    out.append((name, " ".join(parts)))
        if isinstance(node, (ast.For, ast.List, ast.Tuple)):
            if isinstance(node, ast.For):
                seq = node.iter.elts if isinstance(node.iter, (ast.List, ast.Tuple)) else []
            else:
                seq = node.elts
            for elt in seq:
                if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                    if len(elt.value) > 25 and "\n" not in elt.value:
                        out.append(("item", elt.value))


OUT = open(r"C:\Users\HP\Documents\P UI 2\belajar-vue\docs-shots\dump.txt",
           "w", encoding="utf-8")


def emit(s):
    OUT.write(s + "\n")


for f in FILES:
    emit("\n" + "=" * 78)
    emit("FILE: " + f.split("\\")[-1])
    emit("=" * 78)
    tree = ast.parse(open(f, encoding="utf-8").read())
    for fn in tree.body:
        if isinstance(fn, ast.FunctionDef):
            emit("\n--- def %s ---" % fn.name)
            out = []
            collect(fn, out)
            for name, text in out:
                emit("[%s] %s" % (name, text))
        elif isinstance(fn, ast.Expr) and isinstance(fn.value, ast.Call):
            out = []
            collect(fn, out)
            for name, text in out:
                emit("[%s] %s" % (name, text))
OUT.close()
print("dump selesai")
