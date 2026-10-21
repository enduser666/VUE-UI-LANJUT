# -*- coding: utf-8 -*-
"""Isi laporan: BAB II dan BAB III."""


def bab2(R):
    R.h1("BAB II  TINJAUAN PUSTAKA")

    R.h2("2.1  Vue.js dan Composition API")
    R.para("Vue.js adalah framework front-end progresif yang bekerja pada "
           "lapisan tampilan (view layer). Kata progresif pada dokumentasi "
           "resmi Vue.js bermakna bahwa framework ini dapat diadopsi secara "
           "bertahap: mulai dari satu berkas HTML dengan satu berkas "
           "JavaScript, hingga menjadi arsitektur aplikasi lengkap dengan "
           "sistem routing dan manajemen state.")
    R.para("Composition API yang diperkenalkan pada Vue 3 menyediakan cara "
           "mengorganisasi logika komponen secara eksplisit. Setiap komponen "
           "didefinisikan melalui fungsi setup() yang menerima props, lalu "
           "mengembalikan nilai yang akan diekspos ke template. Keunggulan "
           "utama Composition API terletak pada fleksibilitasnya: logika yang "
           "bersifat reusable dapat dipisah ke dalam composable, sehingga "
           "tidak terikat pada pemanggilan siklus hidup komponen tertentu. "
           "Pada laporan ini, logika pengelolaan data event dipisah ke "
           "dalam berkas src/composables/useEvents.js.")
    R.para("Tiga API reaktif yang paling sering digunakan dalam implementasi "
           "ini adalah ref, computed, dan watch. ref digunakan untuk "
           "menyimpan nilai yang dapat berubah dan dapat di-two-way binding "
           "pada input. computed digunakan untuk menghasilkan nilai turunan "
           "yang dihitung otomatis, misalnya daftar event aktif. watch "
           "digunakan untuk melakukan efek samping, yaitu menyimpan state ke "
           "localStorage setiap kali data berubah.")

    R.h2("2.2  Vite sebagai Development Server dan Build Tool")
    R.para("Vite adalah build tool untuk ekosistem JavaScript modern yang "
           "dikembangkan oleh tim yang sama dengan Vue.js. Dua keunggulan "
           "utama Vite dalam konteks praktikum adalah kecepatan start-up "
           "development server dan keluaran produksi yang ringkas.")
    R.para("Pada fase pengembangan, Vite tidak memproses seluruh berkas "
           "aplikasi secara prematur. Sebaliknya, Vite menyajikan berkas "
           "source langsung melalui native ES Module sehingga start-up "
           "server hampir seketika. Pada fase build, Vite menggunakan "
           "Rollup untuk melakukan code splitting, tree-shaking, dan "
           "minification. Mekanisme ini terlihat langsung dari hasil build "
           "pada Tabel 4.4, setiap halaman dipecah menjadi berkas JavaScript "
           "terpisah, sementara bundle utama tetap berukuran ringkas.")

    R.h2("2.3  Vue Router dan Konsep Single Page Application")
    R.para("Vue Router adalah pustaka routing resmi untuk Vue.js yang "
           "menyediakan mekanisme navigasi sisi klien. Dengan Vue Router, aplikasi "
           "dapat berjalan sebagai Single Page Application (SPA), yaitu "
           "aplikasi yang hanya memuat satu dokumen HTML dan melakukan "
           "penggantian tampilan di sisi klien tanpa memuat ulang seluruh "
           "halaman dari server.")
    R.para("Konsekuensi dari pendekatan SPA adalah berkurangnya permintaan "
           "jaringan pada setiap perpindahan halaman, sehingga "
           "kemungkinan aplikasi terasa jauh lebih cepat dan cair. Namun "
           "SPA menuntut pengembang menyusun peta rute secara eksplisit, "
           "sehingga umumnya disertai komponen navigasi seperti Navbar dan "
           "Breadcrumb agar pengguna tidak kehilangan konteks posisi.")

    R.table(
        ["Aspek", "Single Page Application (SPA)", "Multi Page Application (MPA)"],
        [["Definisi", "Satu dokumen HTML, tampilan diganti di sisi klien",
          "Setiap halaman merupakan dokumen HTML terpisah"],
         ["Routing", "Dilakukan oleh Vue Router di sisi klien",
          "Dilakukan oleh server melalui navigasi URL penuh"],
         ["Performa", "Transisi cepat tanpa reload penuh",
          "Setiap perpantian memicu permintaan dokumen baru"],
         ["State", "Dijaga di memori aplikasi, bertahan selama sesi",
          "Tidak ada state sisi klien yang terpusat"],
         ["Kompleksitas", "Memerlukan pengelolaan rute dan orientasi pengguna",
          "Lebih sederhana, namun berpindah antar halaman"]],
        "Tabel 2.1  Perbandingan Konsep Single Page Application dan Multi Page Application",
        widths=[3.0, 5.9, 6.1], size=10)

    R.h2("2.4  Hierarki Parent–Child dalam Navigasi")
    R.para("Pada aplikasi web berskala menengah, sekumpulan halaman tidak "
           "selalu berada pada level yang sama. Sebagian halaman merupakan "
           "kelompok yang memuat sejumlah halaman turunan, misalnya halaman "
           "Browse yang memuat daftar event dan halaman kategori. Relasi "
           "seperti ini dalam Vue Router direpresentasikan melalui properti "
           "children pada objek rute.")
    R.para("Implementasi hierarki Parent–Child memiliki beberapa manfaat "
           "penting. Pertama, outlet dari parent dapat langsung merender "
           "children tanpa mengubah URL, sehingga URL tetap mencerminkan "
           "posisi pengguna secara utuh. Kedua, komponen Breadcrumb dapat "
           "menelusuri properti route.matched untuk membentuk jejak navigasi "
           "otomatis. Ketiga, menu navigasi dapat dibangun dari satu sumber "
           "kebenaran, yaitu array konfigurasi rute, sehingga struktur menu "
           "dan struktur URL tidak pernah berbeda.")

    R.h2("2.5  Komponen Reusable, Props, Emits, dan Slot")
    R.para("Komponen dalam Vue.js adalah unit pembangun antarmuka yang dapat "
           "dipakai ulang. Empat mekanisme komunikasi antar komponen "
           "yang digunakan dalam laporan ini adalah props, emits, slot, dan "
           "v-model.")
    for x in [
        "Props adalah mekanisme aliran data dari parent ke child. Contohnya, "
        "komponen AppButton menerima prop variant untuk menentukan gaya "
        "tombol, dan komponen EventCard menerima prop event berisi detail "
        "acara.",
        "Emits adalah mekanisme aliran data dari child ke parent. Komponen "
        "EventCard memancarkan event view-detail beserta payload id agar "
        "halaman induk dapat mengarahkan pengguna ke halaman detail.",
        "Slot adalah mekanisme penyisipan konten fleksibel. Komponen AppCard "
        "hanya menyediakan kerangka visual, sedangkan isi kartu sepenuhnya "
        "ditentukan oleh pemanggilnya.",
        "v-model adalah jalan pintas atas kombinasi props dan emits yang "
        "bekerja secara dua arah. Komponen SearchBar dan CategoryFilter "
        "mengimplementasikannya melalui prop modelValue dan event "
        "update:modelValue.",
    ]:
        R.bullet(x)

    R.h2("2.6  State Persisten pada localStorage")
    R.para("localStorage adalah penyimpanan sisi klien yang menyimpan "
           "data dalam bentuk string. Pada prototipe aplikasi tanpa server, "
           "localStorage lazim dipakai untuk mengganti basis data sementara "
           "agar data tetap tersedia setelah halaman dimuat ulang. Pada "
           "proyek ini, composable useEvents menyimpan seluruh data event "
           "pada kunci gatherly_events dan menggunakan watcher dengan "
           "opsi deep untuk menyinkronkan perubahan setiap kali state "
           "diperbarui.")


def bab3(R):
    R.h1("BAB III  ANALISIS DAN PERANCANGAN")

    R.h2("3.1  Capaian Pembelajaran Mata Kuliah")
    R.para("Modul 0 dan Modul 1 menetapkan capaian pembelajaran berikut, "
           "yang menjadi dasar penilaian keberhasilan implementasi pada "
           "Bab IV dan Bab V.")
    R.table(
        ["No", "Capaian Pembelajaran Mata Kuliah", "Modul"],
        [["1", "Memahami relasi konseptual antara Site Map, View, dan Router",
          "Modul 1"],
         ["2", "Menerapkan hierarki Parent–Child di dalam struktur aplikasi web",
          "Modul 1"],
         ["3", "Mengimplementasikan pola pergerakan pengguna berupa transisi navigasi",
          "Modul 1"],
         ["4", "Merancang komponen Navbar interaktif menggunakan router-link",
          "Modul 1"],
         ["5", "Merancang komponen Location Indicator (Breadcrumb) untuk orientasi pengguna",
          "Modul 1"],
         ["6", "Menjalankan satu aplikasi Vue utuh yang memuat berbagai halaman pendukung",
          "Modul 1"],
         ["7", "Menyiapkan environment pengembangan dan mengonfigurasi project Vue.js",
          "Modul 0"]],
        "Tabel 3.1  Capaian Pembelajaran Mata Kuliah (CPMK) Modul 0 dan Modul 1",
        widths=[1.2, 11.0, 2.8], size=10)

    R.h2("3.2  Analisis Kebutuhan Fungsional")
    R.para("Aplikasi Gatherly dikembangkan sebagai platform komunitas event "
           "yang memiliki dua sisi penggunaan, yaitu sisi publik untuk "
           "pengunjung dan sisi organizer untuk pengelola acara. Analisis "
           "kebutuhan fungsionalnya dirangkum pada Tabel 3.2, sedangkan "
           "pemetaan terhadap capaian pembelajaran disajikan pada Tabel 3.1.")
    R.table(
        ["Kode", "Kebutuhan Fungsional", "Satisfied By"],
        [["F-01", "Menampilkan halaman utama berisi hero section dan fitur unggulan",
          "Home.vue"],
         ["F-02", "Mengalihkan navigasi antar halaman tanpa reload penuh",
          "router-link pada Navbar.vue"],
         ["F-03", "Menampilkan struktur menu bertingkat sampai dua level",
          "Dropdown dan submenu pada Navbar.vue"],
         ["F-04", "Menampilkan jejak posisi pengguna pada halaman bersarang",
          "Breadcrumb.vue berbasis route.matched"],
         ["F-05", "Mencantumkan katalog event aktif beserta filter pencarian",
          "EventList.vue, SearchBar.vue"],
         ["F-06", "Menyaring event berdasarkan kategori",
          "CategoryFilter.vue"],
         ["F-07", "Menampilkan detail event beserta tombol pendaftaran",
          "EventDetail.vue"],
         ["F-08", "Menampilkan halaman 404 kustom untuk event yang tidak ditemukan",
          "Blok v-else pada EventDetail.vue"],
         ["F-09", "Menyediakan formulir publik untuk menghubungi penyelenggara",
          "Contact.vue"],
         ["F-10", "Menampilkan statistik event pada dasbor organizer",
          "Dashboard.vue"],
         ["F-11", "Mengelola siklus hidup event: membuat, menuntaskan, dan menghapus",
          "EventManagement.vue"],
         ["F-12", "Meminta konfirmasi sebelum tindakan merusak data",
          "AppModal.vue"],
         ["F-13", "Menyimpan data event agar tetap tersedia setelah reload",
          "useEvents.js dengan localStorage"]],
        "Tabel 3.2  Analisis Kebutuhan Fungsional Aplikasi Gatherly",
        widths=[1.6, 9.0, 4.4], size=10)

    R.h2("3.3  Peta Situs (Site Map)")
    R.para("Site Map pada aplikasi Gatherly disusun berdasarkan dua "
           "kelompok navigasi. Kelompok pertama berada di bawah Layout "
           "publik dan terdiri atas Home, About, Browse, dan Contact. "
           "Browse berperan sebagai Destinasi Induk (Parent) yang memuat dua "
           "halaman turunan, yaitu Event List dan Category, dengan Event "
           "List kembali memiliki turunan berupa halaman detail event "
           "berparameter. Kelompok kedua adalah Dasbor Organizer yang "
           "memakai layout terpisah dan memuat halaman Overview serta "
           "Manajemen Event.")
    R.figure("diagram_site_map.png",
             "Gambar 3.1  Peta Situs (Site Map) Aplikasi Gatherly beserta "
             "Hierarki Parent–Child", width_cm=13.4)

    R.h2("3.4  Struktur Folder Project")
    R.para("Pemisahan file pada proyek ini mengikuti empat lapis yang saling "
           "jelas, yaitu entry point, layout, views, dan components. "
           "Struktur lengkap direktori src/ disajikan berikut ini.")
    R.code("""src/
├─  main.js                    Entry point aplikasi
├─  App.vue                    Root component (memuat <RouterView />)
├─  assets/
│   ├─  base.css               Token warna bawaan tema Vue
│   ├─  main.css               Token desain Gatherly + reset global
│   └─  logo.svg               Logo bawaan project
├─  router/
│   └─  index.js               Konfigurasi Vue Router dan tabel rute
├─  layouts/
│   ├─  App.vue                Layout publik (Navbar + Breadcrumb)
│   └─  DashboardLayout.vue    Layout dasbor organizer (sidebar)
├─  stores/
│   └─  counter.js             Store Pinia bawaan generator
├─  composables/
│   └─  useEvents.js           State event reaktif + persistensi localStorage
├─  components/
│   ├─  app/
│   │   ├─  Navbar.vue         Navigasi utama bertingkat
│   │   └─  Breadcrumb.vue     Location Indicator
│   ├─  event/
│   │   ├─  EventCard.vue      Kartu ringkasan event
│   │   ├─  SearchBar.vue      Input pencarian (v-model)
│   │   └─  CategoryFilter.vue Filter kategori (v-model)
│   └─  ui/
│       ├─  AppButton.vue      Tombol dengan variant
│       ├─  AppCard.vue        Wrapper kartu dengan slot
│       └─  AppModal.vue       Modal konfirmasi
└─  views/
    ├─  Home.vue               Destinasi utama
    ├─  About.vue              Destinasi lateral
    ├─  Contact.vue            Destinasi lateral
    ├─  Browse.vue             Destinasi induk (parent)
    ├─  Category.vue           Destinasi anak (sibling)
    ├─  EventList.vue          Destinasi penelusuran
    ├─  EventDetail.vue        Ujung Destinasi
    ├─  Dasboard.vue           Berkas lama (tidak lagi dipakai router)
    ├─  Dashboard.vue          Ringkasan statistik organizer
    └─  EventManagement.vue    Pengelolaan event""",
           caption="Kode 3.1  Struktur Direktori src/ pada Proyek belajar-vue")

    R.h2("3.5  Arsitektur Lapisan Aplikasi")
    R.para("Seluruh aliran data pada aplikasi mengikuti arah satu dari atas "
           "ke bawah. Perubahan URL dicocokkan oleh router, hasil pencocokan "
           "diteruskan ke layout, layout menugaskan outlet untuk merender "
           "view, view menggunakan komponen reusable dan composable, dan "
           "perubahan state pada composable diteruskan ke localStorage. "
           "Arsitektur tersebut divisualisasikan pada Gambar 3.2.")
    R.figure("diagram_arsitektur.png",
             "Gambar 3.2  Arsitektur Lapisan Aplikasi Vue.js pada Proyek "
             "belajar-vue", width_cm=13.4)

    R.h2("3.6  Perancangan Hierarki Navigasi")
    R.para("Array menus pada Navbar.vue menjadi satu sumber kebenaran bagi "
           "seluruh tautan navigasi. Setiap elemen menu memiliki properti "
           "name, path, dan children opsional. Elemen yang memiliki children "
           "akan menampilkan indikator panah dan dropdown, sedangkan elemen "
           "level kedua yang juga memiliki children akan menampilkan "
           "submenu di sisi kanan. Perancangan ini disajikan pada Gambar "
           "3.3.")
    R.figure("diagram_hierarki_nav.png",
             "Gambar 3.3  Perancangan Hierarki Navigasi pada Komponen "
             "Navbar.vue", width_cm=13.4)

    R.h2("3.7  Perancangan Komponen Reusable")
    R.para("Komponen reusable pada proyek ini dikelompokkan ke dalam tiga "
           "folder berdasarkan domain penggunaannya, yaitu app untuk "
           "komponen tingkat aplikasi, event untuk komponen domain acara, dan "
           "ui untuk komponen generik. Pengelompokan ini memudahkan "
           "penelusuran dan mencegah duplikasi. Kontrak antarkomponen "
           "dirangkum pada Tabel 3.3 dan Gambar 3.4.")
    R.table(
        ["Komponen", "Props", "Emits", "Peran"],
        [["AppButton", "variant (primary | secondary)", "—",
          "Tombol generik dengan gaya yang seragam"],
         ["AppCard", "—", "—", "Pembungkus kartu yang menerima slot"],
         ["AppModal", "isOpen, title, message, confirmText, cancelText",
          "confirm, close", "Dialog konfirmasi dengan efek transisi"],
         ["EventCard", "event (Object)", "view-detail (payload: id)",
          "Kartu ringkasan event pada katalog publik"],
         ["SearchBar", "modelValue (String)", "update:modelValue",
          "Input pencarian dua arah"],
         ["CategoryFilter", "categories (Array), modelValue (String)",
          "update:modelValue", "Dropdown filter kategori"],
         ["Navbar", "—", "—", "Navigasi utama bertingkat"],
         ["Breadcrumb", "—", "—", "Location Indicator otomatis"]],
        "Tabel 3.3  Kontrak Props dan Emits Antarkomponen",
        widths=[3.0, 4.4, 3.2, 4.4], size=9.5)
    R.figure("diagram_komponen.png",
             "Gambar 3.4  Pengelompokan Komponen Reusable pada Direktori "
             "src/components", width_cm=13.4)

    R.h2("3.8  Alur Setup Environment Modul 0")
    R.para("Rangkaian persiapan yang dilakukan praktikan mengikuti alur "
           "pada handout Modul 0, yaitu persiapan perangkat, instalasi "
           "Visual Studio Code, instalasi Node.js dan npm, pemasangan "
           "ekstensi Vue (Official), pembuatan kerangka project, serta "
           "penjalankan server pengembangan. Alur tersebut diringkas pada "
           "Gambar 3.5.")
    R.figure("diagram_alur_modul0.png",
             "Gambar 3.5  Alur Setup Environment Praktikum Modul 0",
             width_cm=13.4)

    R.h2("3.9  Daftar Rute Aplikasi")
    R.para("Tabel rute pada src/router/index.js merupakan definisi formal "
           "dari peta situs. Seluruh rute menggunakan lazy import melalui "
           "fungsi dinamis import() agar berkas view tidak dimuat sebelum "
           "benar-benar dibutuhkan. Rincian setiap rute disajikan pada "
           "Tabel 3.3.")
    R.table(
        ["No", "Path", "Name", "Level", "Komponen"],
        [["1", "/", "home", "1", "layouts/App.vue → views/Home.vue"],
         ["2", "/about", "about", "1", "layouts/App.vue → views/About.vue"],
         ["3", "/browse", "browse", "1", "layouts/App.vue → views/Browse.vue"],
         ["4", "/browse/events", "events", "2", "views/EventList.vue"],
         ["5", "/browse/events/:id", "event-detail", "3", "views/EventDetail.vue"],
         ["6", "/browse/category", "category", "2", "views/Category.vue"],
         ["7", "/contact", "contact", "1", "layouts/App.vue → views/Contact.vue"],
         ["8", "/dashboard", "dashboard-overview", "1",
          "layouts/DashboardLayout.vue → views/Dashboard.vue"],
         ["9", "/dashboard/events", "dashboard-events", "2",
          "views/EventManagement.vue"]],
        "Tabel 3.4  Daftar Rute Aplikasi pada src/router/index.js",
        widths=[1.0, 3.6, 3.2, 1.4, 5.8], size=9.5)

    R.h2("3.10  Spesifikasi Teknis Proyek")
    R.table(
        ["Aspek", "Keterangan"],
        [["Framework", "Vue 3.5 (Composition API, script setup)"],
         ["Routing", "Vue Router 5 dengan createWebHistory"],
         ["State Management", "Pinia 4 (store bawaan) dan composable useEvents"],
         ["Build Tool", "Vite 8 dengan plugin @vitejs/plugin-vue"],
         ["Formatting", "Prettier 3.9.6 (semi: false, singleQuote: true, "
                        "printWidth: 100)"],
         ["Bahasa", "JavaScript ES Module dengan alias path @/"],
         ["Persistensi", "localStorage pada kunci gatherly_events"],
         ["Desain", "Design token CSS berbasis custom property pada "
                    "src/assets/main.css"],
         ["Runtime Praktikan", "Node.js v22.15.1, npm 10.9.2, Vite 8.3.1"],
         ["Browser Uji", "Chromium (engine 138), lebar viewport 1000–1219 piksel"]],
        "Tabel 3.5  Spesifikasi Teknis Proyek belajar-vue",
        widths=[4.0, 11.0], size=10)
