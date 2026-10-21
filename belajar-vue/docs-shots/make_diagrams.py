"""Generator diagram untuk Laporan Praktikum Pengembangan UI Lanjut (Modul 0 & 1).
Output: diagram_site_map.png, diagram_arsitektur.png, diagram_alur_modul0.png,
        diagram_hierarki_nav.png, diagram_komponen.png
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.dirname(os.path.abspath(__file__))

PRIMARY = "#6644ff"
NAVY = "#1c1948"
MUTED = "#666666"
LIGHT = "#f4f4f5"
BORDER = "#d4d4d8"
GREEN = "#27ae60"
RED = "#e63946"
FONT = "Segoe UI"

plt.rcParams["font.family"] = FONT
plt.rcParams["font.size"] = 9


def box(ax, x, y, w, h, text, fc=LIGHT, ec=BORDER, tc=NAVY, fs=9, bold=False, r=0.02):
    p = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.012,rounding_size={r}",
        linewidth=1.2, edgecolor=ec, facecolor=fc, zorder=2,
    )
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs, color=tc, zorder=3,
            fontweight="bold" if bold else "normal", linespacing=1.5)


def line(ax, pts, color=BORDER, lw=1.3, style="-", zorder=1):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    ax.plot(xs, ys, color=color, linewidth=lw, linestyle=style, zorder=zorder,
            solid_capstyle="round")


def arrow(ax, p1, p2, color=MUTED, lw=1.3):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=11,
                                 linewidth=lw, color=color, zorder=1,
                                 shrinkA=0, shrinkB=0))


def canvas(w=12.5, h=6.6):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100 * h / w)
    ax.axis("off")
    return fig, ax


# ---------------------------------------------------------------- 1. SITE MAP
def site_map():
    fig, ax = canvas(12.5, 6.2)
    Y = 100 * 6.2 / 12.5

    box(ax, 41, Y - 9, 18, 7, "/", fc=PRIMARY, ec=PRIMARY, tc="white", fs=12, bold=True)
    ax.text(50, Y - 0.6, "HOME  (Layout: App.vue)", ha="center", va="bottom",
            fontsize=8.5, color=MUTED, style="italic")

    lvl1 = [
        (4.0, "/about", "About", "Lateral"),
        (25.0, "/browse", "Browse", "Induk / Parent"),
        (50.0, "/contact", "Contact", "Lateral"),
        (71.0, "/dashboard", "Organizer\nDashboard", "Layout: Dashboard"),
    ]
    for x, path, name, note in lvl1:
        box(ax, x, Y - 26, 20, 7, f"{name}\n{path}", fc="#ffffff", ec=PRIMARY, fs=8.5, bold=True)
        ax.text(x + 10, Y - 27.6, note, ha="center", va="top", fontsize=7, color=MUTED, style="italic")
        line(ax, [(50, Y - 9), (50, Y - 13), (x + 10, Y - 13), (x + 10, Y - 19)])
    line(ax, [(50, Y - 13), (14, Y - 13)])
    line(ax, [(50, Y - 13), (35, Y - 13)])
    line(ax, [(50, Y - 13), (60, Y - 13)])
    line(ax, [(50, Y - 13), (81, Y - 13)])
    line(ax, [(50, Y - 13), (81, Y - 13)])
    line(ax, [(50, Y - 13), (50, Y - 13)])

    # Browse children
    bx = 25.0
    children = [
        (18.0, "/browse/events", "Event List", "Anak / Child"),
        (38.0, "/browse/category", "Category", "Anak / Sibling"),
    ]
    for x, path, name, note in children:
        box(ax, x, Y - 42, 18, 6.4, f"{name}\n{path}", fc="#ffffff", ec=GREEN, fs=8.5, bold=True)
        ax.text(x + 9, Y - 43.4, note, ha="center", va="top", fontsize=7, color=MUTED, style="italic")
        line(ax, [(bx + 10, Y - 19), (bx + 10, Y - 33), (x + 9, Y - 33), (x + 9, Y - 35.6)])
    line(ax, [(bx + 10, Y - 33), (27, Y - 33)])
    line(ax, [(bx + 10, Y - 33), (47, Y - 33)])

    # Event Detail
    box(ax, 18.0, Y - 55, 18, 6.4, "Event Detail\n/browse/events/:id", fc="#ffffff", ec=RED, fs=8.5, bold=True)
    ax.text(27, Y - 56.4, "Ujung Destinasi", ha="center", va="top", fontsize=7, color=MUTED, style="italic")
    line(ax, [(27, Y - 35.6), (27, Y - 48.6)])

    # Dashboard children
    for x, path, name in [(71.0, "/dashboard", "Overview"), (81.0, "/dashboard/events", "Event Management")]:
        box(ax, x, Y - 42, 9.0, 6.4, f"{name}\n{path}", fc="#ffffff", ec=GREEN, fs=7.6, bold=True)
        line(ax, [(81, Y - 19), (81, Y - 33), (x + 4.5, Y - 33), (x + 4.5, Y - 35.6)])

    ax.text(2, 1.5, "Garis penuh = relasi Parent-Child pada src/router/index.js.  "
                    "Breadcrumb (Location Indicator) diturunkan dari route.matched + meta.breadcrumb.",
            fontsize=7.5, color=MUTED, style="italic")
    fig.savefig(os.path.join(OUT, "diagram_site_map.png"), dpi=220, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------- 2. ARSITEKTUR
def arsitektur():
    fig, ax = canvas(12.5, 6.8)
    Y = 100 * 6.8 / 12.5

    layers = [
        (Y - 8.5, 6.8, "src/App.vue  —  Root Component", PRIMARY, "white",
         "Pusat kanvas aplikasi; membungkus seluruh outlet navigasi"),
        (Y - 19.5, 8.4, "src/layouts/  —  Kerangka Halaman", "#ffffff", NAVY,
         "App.vue (publik + Navbar + Breadcrumb)   |   DashboardLayout.vue (sidebar organizer)"),
        (Y - 31.0, 8.8, "src/views/  —  Destinasi Halaman", "#ffffff", NAVY,
         "Home  ·  About  ·  Browse (Parent)  ·  Category  ·  EventList  ·  EventDetail  ·  Contact  ·  Dashboard  ·  EventManagement"),
        (Y - 43.5, 9.0, "src/components/  —  Komponen Reusable", "#ffffff", NAVY,
         "app/ (Navbar, Breadcrumb)   ·   event/ (EventCard, SearchBar, CategoryFilter)   ·   ui/ (AppButton, AppCard, AppModal)"),
        (Y - 55.0, 7.2, "src/router/index.js  —  Peta Navigasi", NAVY, "white",
         "createRouter + createWebHistory; 8 route dengan children (Parent-Child) dan lazy import"),
        (Y - 64.5, 6.6, "src/composables/ + src/stores/  —  State", "#ffffff", NAVY,
         "useEvents.js (reaktif + persist localStorage)   ·   stores/counter.js (Pinia)   ·   src/assets/ (base.css, main.css)"),
    ]

    for y, h, title, fc, tc, desc in layers:
        box(ax, 3, y, 94, h, "", fc=fc, ec=NAVY if fc == "#ffffff" else fc, r=0.012)
        ax.text(5, y + h - 2.4, title, ha="left", va="top", fontsize=9.5,
                color=tc, fontweight="bold")
        ax.text(5, y + h - 5.4, desc, ha="left", va="top", fontsize=7.8,
                color="#ffffff" if tc == "white" else MUTED)
        if y > Y - 64:
            arrow(ax, (50, y + h + 0.2), (50, y + h + 2.4), color=BORDER, lw=1.1)

    ax.text(3, 1.0, "Aliran data satu arah (top-down): perubahan URL -> Router -> Layout -> View -> Component -> Composable (state) -> localStorage.",
            fontsize=7.5, color=MUTED, style="italic")
    fig.savefig(os.path.join(OUT, "diagram_arsitektur.png"), dpi=220, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------ 3. ALUR MODUL 0
def alur_modul0():
    fig, ax = canvas(12.5, 3.6)
    Y = 100 * 3.6 / 12.5

    steps = [
        ("1. Persiapan\nPerangkat", "OS Win 10/11\nakses admin\ninternet stabil"),
        ("2. Instalasi\nVS Code", "unduh .exe\nofficial\nAdd to PATH"),
        ("3. Instalasi\nNode.js & npm", "versi LTS\nnode -v / npm -v\nverifikasi"),
        ("4. Ekstensi\nVue (Official)", "Ctrl+Shift+X\ncari \"Vue (Official)\"\nInstall"),
        ("5. Generate\nProject", "npm create vue@latest\nnama: belajar-vue\nRouter + Pinia + Prettier"),
        ("6. Install &\nRun", "npm install\nnpm run dev\nlocalhost:5173"),
    ]
    n = len(steps)
    w = 14.0
    gap = (100 - 6 - n * w) / (n - 1)
    for i, (t, d) in enumerate(steps):
        x = 3 + i * (w + gap)
        fc = PRIMARY if i == n - 1 else "#ffffff"
        tc = "white" if i == n - 1 else NAVY
        box(ax, x, Y - 26, w, 13, "", fc=fc, ec=PRIMARY, r=0.012)
        ax.text(x + w / 2, Y - 15.5, t, ha="center", va="center", fontsize=8.6,
                color=tc, fontweight="bold", linespacing=1.4)
        ax.text(x + w / 2, Y - 23.2, d, ha="center", va="center", fontsize=7.2,
                color="#e9e4ff" if i == n - 1 else MUTED, linespacing=1.5)
        if i < n - 1:
            arrow(ax, (x + w + 0.6, Y - 19.5), (x + w + gap - 0.6, Y - 19.5), color=MUTED)

    ax.text(3, 2.0, "Alur setup environment (Modul 0) yang dijalankan pada mesin praktikan: Node.js v22.15.1 · npm 10.9.2 · Vite 8.3.1.",
            fontsize=7.5, color=MUTED, style="italic")
    fig.savefig(os.path.join(OUT, "diagram_alur_modul0.png"), dpi=220, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


# ------------------------------------------------------- 4. HIERARKI NAVBAR
def hierarki_nav():
    fig, ax = canvas(12.5, 4.4)
    Y = 100 * 4.4 / 12.5

    box(ax, 38, Y - 9, 24, 6.5, "Navbar.vue", fc=NAVY, ec=NAVY, tc="white", fs=10, bold=True)
    ax.text(50, Y - 10.4, "src/components/app/Navbar.vue", ha="center", va="top",
            fontsize=7.2, color=MUTED, style="italic")

    menus = [
        (2.5, "Home", "/", None),
        (17.0, "About", "/about", None),
        (31.5, "Browse", "/browse", "Parent (Level 1)"),
        (56.0, "Contact", "/contact", None),
        (70.5, "Organizer\nDashboard", "/dashboard", "Layout terpisah"),
    ]
    for x, name, path, note in menus:
        box(ax, x, Y - 24, 13, 7, f"{name}\n{path}", fc="#ffffff", ec=PRIMARY, fs=8, bold=True)
        line(ax, [(50, Y - 9), (50, Y - 13), (x + 6.5, Y - 13), (x + 6.5, Y - 17)])
        if note:
            ax.text(x + 6.5, Y - 25.4, note, ha="center", va="top", fontsize=7,
                    color=MUTED, style="italic")
    line(ax, [(50, Y - 13), (9, Y - 13)])
    line(ax, [(50, Y - 13), (23.5, Y - 13)])
    line(ax, [(50, Y - 13), (38, Y - 13)])
    line(ax, [(50, Y - 13), (62.5, Y - 13)])
    line(ax, [(50, Y - 13), (77, Y - 13)])

    subs = [
        (24.0, "Event List", "/browse/events", "Submenu (Level 2)"),
        (44.0, "Category", "/browse/category", "Submenu (Level 2)"),
    ]
    for x, name, path, note in subs:
        box(ax, x, Y - 40, 18, 6.5, f"{name}\n{path}", fc="#ffffff", ec=GREEN, fs=8, bold=True)
        line(ax, [(38, Y - 24), (38, Y - 34), (x + 9, Y - 34), (x + 9, Y - 33.5)])
        ax.text(x + 9, Y - 41.2, note, ha="center", va="top", fontsize=7,
                color=MUTED, style="italic")
    line(ax, [(38, Y - 34), (33, Y - 34)])
    line(ax, [(38, Y - 34), (53, Y - 34)])

    box(ax, 66.0, Y - 40, 18, 6.5, "Event Detail\n/browse/events/:id", fc="#ffffff", ec=RED, fs=8, bold=True)
    line(ax, [(33, Y - 33.5), (33, Y - 37), (75, Y - 37), (75, Y - 33.5)])
    ax.text(75, Y - 41.2, "Ujung / level terdalam", ha="center", va="top", fontsize=7,
            color=MUTED, style="italic")

    ax.text(2, 1.5, "Menu dropdown diaktifkan dengan CSS :hover pada .nav-item (Level 1) dan .dropdown-item (Level 2); "
                    "state active menandai rute yang sedang dibuka.", fontsize=7.5, color=MUTED, style="italic")
    fig.savefig(os.path.join(OUT, "diagram_hierarki_nav.png"), dpi=220, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


# --------------------------------------------------------- 5. KOMPONEN REUSE
def komponen():
    fig, ax = canvas(12.5, 4.6)
    Y = 100 * 4.6 / 12.5

    box(ax, 36, Y - 8, 28, 6.5, "src/components/", fc=NAVY, ec=NAVY, tc="white", fs=10, bold=True)

    groups = [
        (3.0, "app/", "Navbar.vue\nBreadcrumb.vue", PRIMARY),
        (26.0, "event/", "EventCard.vue\nSearchBar.vue\nCategoryFilter.vue", GREEN),
        (52.0, "ui/", "AppButton.vue\nAppCard.vue\nAppModal.vue", "#d97706"),
        (78.0, "Layout & Store", "layouts/App.vue\ncomposables/useEvents.js", MUTED),
    ]
    for x, name, items, col in groups:
        box(ax, x, Y - 24, 19, 13, "", fc="#ffffff", ec=col, r=0.012)
        ax.text(x + 9.5, Y - 15.5, name, ha="center", va="center", fontsize=9,
                color=col, fontweight="bold")
        ax.text(x + 9.5, Y - 22.0, items, ha="center", va="center", fontsize=7.4,
                color=NAVY, linespacing=1.6)
        line(ax, [(50, Y - 8), (50, Y - 11), (x + 9.5, Y - 11), (x + 9.5, Y - 11)])

    ax.text(3, 1.5, "Kontrak props / event antar komponen: AppButton { variant } · AppCard { slot } · AppModal { isOpen, title, message } "
                    "· SearchBar & CategoryFilter { modelValue } · EventCard { event } + emit('view-detail').",
            fontsize=7.4, color=MUTED, style="italic")
    fig.savefig(os.path.join(OUT, "diagram_komponen.png"), dpi=220, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    site_map()
    arsitektur()
    alur_modul0()
    hierarki_nav()
    komponen()
    print("diagrams generated")
    for f in sorted(os.listdir(OUT)):
        if f.startswith("diagram_"):
            print(" -", f, os.path.getsize(os.path.join(OUT, f)))
