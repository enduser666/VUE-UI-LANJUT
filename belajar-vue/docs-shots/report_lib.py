# -*- coding: utf-8 -*-
"""Helper pembentuk dokumen .docx untuk laporan praktikum (format akademik)."""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY = RGBColor(0x1C, 0x19, 0x48)
PRIMARY = RGBColor(0x66, 0x44, 0xFF)
GREY = RGBColor(0x55, 0x55, 0x55)
BLACK = RGBColor(0x00, 0x00, 0x00)
CODE_BG = "F4F4F5"
HEAD_BG = "EDE9FE"
TBL_BG = "F5F5F7"

# lebar area konten: A4 (21 cm) - margin kiri (4 cm) - margin kanan (3 cm)
CONTENT_W_CM = 13.4

ALIGN = {
    "justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
    "center": WD_ALIGN_PARAGRAPH.CENTER,
    "right": WD_ALIGN_PARAGRAPH.RIGHT,
    "left": WD_ALIGN_PARAGRAPH.LEFT,
}


class Report:
    def __init__(self, out_path, images_dir=None, code_font="Consolas"):
        self.out_path = out_path
        self.images_dir = images_dir
        self.code_font = code_font
        self.doc = Document()
        self._setup_page()
        self._setup_styles()

    # ------------------------------------------------------------- internals
    def _setup_page(self):
        s = self.doc.sections[0]
        s.page_width = Cm(21.0)
        s.page_height = Cm(29.7)
        s.top_margin = Cm(3.0)
        s.bottom_margin = Cm(2.5)
        s.left_margin = Cm(4.0)
        s.right_margin = Cm(3.0)
        s.header_distance = Cm(1.5)
        s.footer_distance = Cm(1.3)

        n = self.doc.styles["Normal"]
        n.font.name = "Times New Roman"
        n.font.size = Pt(12)
        n.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
        n.paragraph_format.line_spacing = 1.5
        n.paragraph_format.space_after = Pt(0)

        for name, size, color, bold, caps in [
            ("Heading 1", 14, NAVY, True, True),
            ("Heading 2", 13, NAVY, True, False),
            ("Heading 3", 12, PRIMARY, True, False),
        ]:
            st = self.doc.styles[name]
            st.font.name = "Times New Roman"
            st.font.size = Pt(size)
            st.font.bold = bold
            st.font.color.rgb = color
            st.font.all_caps = caps
            st.paragraph_format.space_before = Pt(14 if name == "Heading 1" else 10)
            st.paragraph_format.space_after = Pt(6)
            st.paragraph_format.line_spacing = 1.3
            st.paragraph_format.keep_with_next = True
            st.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")

    def _setup_styles(self):
        # footer: "Halaman N"
        p = self.doc.sections[0].footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("Halaman ")
        self._font(r, "Times New Roman", 10, color=GREY)
        self._field(p, "PAGE", 10)

        # halaman judul (halaman pertama) tanpa nomor halaman
        sectPr = self.doc.sections[0]._sectPr
        titlePg = OxmlElement("w:titlePg")
        sectPr.append(titlePg)

        settings = self.doc.settings.element
        el = OxmlElement("w:updateFields")
        el.set(qn("w:val"), "true")
        settings.append(el)

    @staticmethod
    def _font(run, name="Times New Roman", size=12, bold=False, italic=False,
              color=BLACK):
        run.font.name = name
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = color
        rpr = run._element.get_or_add_rPr()
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = OxmlElement("w:rFonts")
            rpr.append(rfonts)
        for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
            rfonts.set(qn(attr), name)

    @staticmethod
    def _shade(element, hexcolor):
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), hexcolor)
        element.append(shd)

    @staticmethod
    def _border(p, color="D4D4D8", sz="6", sides=("top", "left", "bottom", "right")):
        ppr = p._p.get_or_add_pPr()
        borders = OxmlElement("w:pBdr")
        for s in sides:
            el = OxmlElement("w:" + s)
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), sz)
            el.set(qn("w:space"), "6")
            el.set(qn("w:color"), color)
            borders.append(el)
        ppr.append(borders)

    @staticmethod
    def _keep_next(p):
        ppr = p._p.get_or_add_pPr()
        ppr.append(OxmlElement("w:keepNext"))

    def _field(self, paragraph, instr, size=11):
        r1 = paragraph.add_run()
        fc = OxmlElement("w:fldChar")
        fc.set(qn("w:fldCharType"), "begin")
        r1._r.append(fc)
        r2 = paragraph.add_run()
        it = OxmlElement("w:instrText")
        it.set(qn("xml:space"), "preserve")
        it.text = instr
        r2._r.append(it)
        r3 = paragraph.add_run()
        fs = OxmlElement("w:fldChar")
        fs.set(qn("w:fldCharType"), "separate")
        r3._r.append(fs)
        r4 = paragraph.add_run("1")
        r5 = paragraph.add_run()
        fe = OxmlElement("w:fldChar")
        fe.set(qn("w:fldCharType"), "end")
        r5._r.append(fe)
        self._font(r4, "Times New Roman", size)
        return r4

    # --------------------------------------------------------------- writers
    def para(self, text="", size=12, bold=False, italic=False, align="justify",
             indent=1.27, space_after=6, line=1.5, color=BLACK,
             font="Times New Roman", space_before=0, left_indent=0.0):
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        pf.line_spacing = line
        pf.space_after = Pt(space_after)
        pf.space_before = Pt(space_before)
        if left_indent:
            pf.left_indent = Cm(left_indent)
        p.alignment = ALIGN[align]
        if indent and align == "justify":
            pf.first_line_indent = Cm(indent)
        if text:
            self._font(p.add_run(text), font, size, bold, italic, color)
        return p

    def rich(self, parts, align="justify", indent=1.27, size=12, space_after=6,
             line=1.5):
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        pf.line_spacing = line
        pf.space_after = Pt(space_after)
        p.alignment = ALIGN[align]
        if indent:
            pf.first_line_indent = Cm(indent)
        for item in parts:
            text, bold, italic = (item + (False, False))[:3] if len(item) < 3 else item
            self._font(p.add_run(text), "Times New Roman", size, bold, italic, BLACK)
        return p

    def h1(self, text, page_break=True):
        if page_break:
            self.doc.add_page_break()
        p = self.doc.add_heading(text, level=1)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            self._font(r, "Times New Roman", 14, True, False, NAVY)
        p.paragraph_format.space_after = Pt(12)
        return p

    def h2(self, text):
        p = self.doc.add_heading(text, level=2)
        for r in p.runs:
            self._font(r, "Times New Roman", 13, True, False, NAVY)
        return p

    def h3(self, text):
        p = self.doc.add_heading(text, level=3)
        for r in p.runs:
            self._font(r, "Times New Roman", 12, True, False, PRIMARY)
        return p

    def bullet(self, text, level=0, size=12, style="List Bullet"):
        p = self.doc.add_paragraph(style=style)
        pf = p.paragraph_format
        pf.left_indent = Cm(1.0 + 0.75 * level)
        pf.first_line_indent = Cm(-0.6)
        pf.line_spacing = 1.4
        pf.space_after = Pt(3)
        self._font(p.add_run(text), "Times New Roman", size)
        return p

    def numbered(self, text, size=12):
        return self.bullet(text, size=size, style="List Number")

    def code(self, text, size=9.0, caption=None):
        if caption:
            cp = self.para(caption, size=11, bold=True, align="left", indent=0,
                           space_after=2, line=1.2, space_before=8)
            self._keep_next(cp)
        lines = text.strip("\n").split("\n")
        for i, ln in enumerate(lines):
            p = self.doc.add_paragraph()
            pf = p.paragraph_format
            pf.line_spacing = 1.05
            pf.space_after = Pt(0)
            pf.space_before = Pt(4) if i == 0 else Pt(0)
            pf.left_indent = Cm(0.4)
            pf.right_indent = Cm(0.2)
            if i == len(lines) - 1:
                pf.space_after = Pt(10)
            self._font(p.add_run(ln if ln.strip() else " "), self.code_font, size,
                       False, False, RGBColor(0x1C, 0x19, 0x48))
            self._shade(p._p.get_or_add_pPr(), CODE_BG)
            self._border(p)
            if i < len(lines) - 1:
                self._keep_next(p)
        return None

    def figure(self, filename, caption, width_cm=13.5):
        path = os.path.join(self.images_dir, filename) if self.images_dir else filename
        if not os.path.exists(path):
            self.para("[Gambar tidak ditemukan: %s]" % filename, italic=True,
                      align="center", indent=0)
            return
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        self._keep_next(p)
        p.add_run().add_picture(path, width=Cm(width_cm))
        cp = self.doc.add_paragraph()
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cp.paragraph_format.space_after = Pt(12)
        self._font(cp.add_run(caption), "Times New Roman", 10, True, False, BLACK)

    def table(self, headers, rows, caption=None, widths=None, size=10,
              align_first_left=True, header=True):
        if caption:
            cp = self.para(caption, size=11, bold=True, align="left", indent=0,
                           space_after=3, line=1.2, space_before=10)
            self._keep_next(cp)
        if widths:
            scale = min(1.0, CONTENT_W_CM / float(sum(widths)))
            widths = [round(w * scale, 2) for w in widths]
        t = self.doc.add_table(rows=0, cols=len(headers))
        t.style = "Table Grid"
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        self._fixed_layout(t, widths)
        if header:
            cells = t.add_row().cells
            for i, htext in enumerate(headers):
                cells[i].text = ""
                p = cells[i].paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.space_before = Pt(2)
                self._font(p.add_run(htext), "Times New Roman", size, True, False, NAVY)
                self._shade(cells[i]._tc.get_or_add_tcPr(), HEAD_BG)
        for ri, row in enumerate(rows):
            cells = t.add_row().cells
            for i, val in enumerate(row):
                cells[i].text = ""
                p = cells[i].paragraphs[0]
                p.alignment = (WD_ALIGN_PARAGRAPH.LEFT
                               if (i == 0 and align_first_left)
                               else WD_ALIGN_PARAGRAPH.CENTER)
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.space_before = Pt(2)
                self._font(p.add_run(str(val)), "Times New Roman", size)
                if ri % 2 == 1:
                    self._shade(cells[i]._tc.get_or_add_tcPr(), TBL_BG)
        if widths:
            for i, w in enumerate(widths):
                for row in t.rows:
                    row.cells[i].width = Cm(w)
        sp = self.doc.add_paragraph()
        sp.paragraph_format.space_after = Pt(10)
        return t

    @staticmethod
    def _fixed_layout(t, widths=None):
        """Paksa layout tabel fixed agar lebar kolom tidak dihitung ulang Word."""
        tbl = t._tbl
        tblPr = tbl.tblPr

        def upsert(tag, attrs, successors):
            el = tblPr.find(qn(tag))
            if el is None:
                el = OxmlElement(tag)
                tblPr.insert_element_before(el, *successors)
            for k, v in attrs.items():
                el.set(qn(k), v)
            return el

        upsert("w:tblW",
               {"w:w": str(int(CONTENT_W_CM * 567)), "w:type": "dxa"},
               ("w:jc", "w:tblCellSpacing", "w:tblInd", "w:tblBorders", "w:shd",
                "w:tblLayout", "w:tblCellMar", "w:tblLook"))
        upsert("w:tblInd", {"w:w": "0", "w:type": "dxa"},
               ("w:tblBorders", "w:shd", "w:tblLayout", "w:tblCellMar",
                "w:tblLook"))
        upsert("w:tblLayout", {"w:type": "fixed"},
               ("w:tblCellMar", "w:tblLook"))

        # margin sel lebih rapat supaya tabel tidak melewati margin kanan
        cm = tblPr.find(qn("w:tblCellMar"))
        if cm is None:
            cm = OxmlElement("w:tblCellMar")
            tblPr.insert_element_before(cm, "w:tblLook")
        for side, val in (("top", 28), ("left", 85), ("bottom", 28), ("right", 85)):
            e = cm.find(qn("w:" + side))
            if e is None:
                e = OxmlElement("w:" + side)
                cm.append(e)
            e.set(qn("w:w"), str(val))
            e.set(qn("w:type"), "dxa")

        # lebar kolom pada w:tblGrid
        grid = tbl.find(qn("w:tblGrid"))
        if grid is not None and widths:
            cols = grid.findall(qn("w:gridCol"))
            if len(cols) == len(widths):
                for c, w in zip(cols, widths):
                    c.set(qn("w:w"), str(int(round(w * 567))))

    def toc(self, levels='1-2'):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        self._font(p.add_run("Daftar isi di bawah ini adalah field otomatis. Untuk "
                             "memperbarui nomor halaman, klik kanan pada tabel "
                             "dan pilih â€œUpdate Fieldâ€."),
                  "Times New Roman", 10, False, True, GREY)
        p2 = self.doc.add_paragraph()
        self._field(p2, 'TOC \\o "%s" \\h \\z \\u' % levels, 11)

    def page_break(self):
        self.doc.add_page_break()

    def blank(self, n=1):
        for _ in range(n):
            self.doc.add_paragraph()

    def save(self):
        self.doc.save(self.out_path)
        return self.out_path
