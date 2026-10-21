# -*- coding: utf-8 -*-
"""Isi laporan: BAB IV, BAB V, BAB VI, Daftar Pustaka, dan Lampiran."""


def bab4(R):
    R.h1("BAB IV  IMPLEMENTASI")

    R.h2("4.1  Modul 0: Instalasi dan Konfigurasi Environment")
    R.para("Tahap pertama yang dilakukan adalah penyiapan environment "
           "pengembangan. Visual Studio Code dipasang sebagai editor teks "
           "utama, sedangkan Node.js dan npm berperan sebagai penyedia "
           "runtime JavaScript. Sesuai panduan modul, versi Long Term "
           "Support (LTS) dipilih karena dianggap paling stabil untuk "
           "pembelajar. Ekstensi Vue (Official) kemudian dipasang agar "
           "editor dapat menyorot sintaks berkas .vue dan memberikan "
           "petunjuk kode.")
    R.para("Setelah environment siap, kerangka project dibuat dengan "
           "perintah npm create vue@latest. Generator akan menampilkan "
           "sejumlah pertanyaan konfigurasi, dan jawaban yang dipilih pada "
           "praktikum ini dirangkum pada Tabel 4.1.")
    R.table(
        ["Pertanyaan Generator", "Pilihan", "Alasan"],
        [["Project name", "belajar-vue", "Mengikuti nama project pada modul"],
         ["Use TypeScript?", "No", "Menggunakan JavaScript agar lebih mudah dipahami"],
         ["JSX Support", "No", "Menggunakan sintaks template standar Vue"],
         ["Router (SPA)", "Yes", "Menjadi dasar navigasi dan pemetaan Site Map"],
         ["Pinia (state management)", "Yes", "Menyediakan manajemen state terpusat"],
         ["Vitest (unit testing)", "No", "Modul tidak berfokus pada pengujian otomatis"],
         ["End-to-End Testing", "No", "Tidak diperlukan pada tahap ini"],
         ["Linter", "No", "Mempertahankan konfigurasi tetap sederhana"],
         ["Prettier", "Yes", "Menjaga format kode tetap rapi dan konsisten"],
         ["Replace Prettier with Oxfmt", "No", "Mempertahankan fokus pada konsep inti Vue"],
         ["Vue 3.6 (Release Candidate)", "No", "Menggunakan versi framework yang stabil"],
         ["Skip all example code", "No", "Mempertahankan contoh kode bawaan sebagai referensi"]],
        "Tabel 4.1  Konfigurasi Project pada Generator create-vue",
        widths=[4.6, 2.4, 8.0], size=9.5)

    R.para("Setelah generator selesai, langkah berikutnya adalah masuk ke "
           "direktori project, mengunduh seluruh dependensi, merapikan "
           "format kode, dan menjalankan server pengembangan. Perintah yang "
           "digunakan beserta fungsinya dirangkum berikut ini.")
    R.code("""cd belajar-vue
npm install
npm run format
npm run dev""",
           caption="Kode 4.1  Rangkaian Perintah Preparation dan Run Server")
    R.para("Development server Vite berjalan pada alamat http://localhost:5173 "
           "secara default. Selama server aktif, setiap perubahan pada berkas "
           "sumber akan langsung tercermin di browser melalui fitur hot "
           "reload. Proses server dihentikan dengan kombinasi tombol Ctrl + C "
           "pada terminal.")
    R.table(
        ["Komponen", "Perintah Verifikasi", "Hasil pada Mesin Praktikan"],
        [["Node.js", "node -v", "v22.15.1"],
         ["npm", "npm -v", "10.9.2"],
         ["Vite", "npx vite --version", "8.3.1"],
         ["Vue", "npm ls vue", "3.5.42"],
         ["Vue Router", "npm ls vue-router", "5.3.1"],
         ["Pinia", "npm ls pinia", "4.0.3"],
         ["Prettier", "npm ls prettier", "3.9.6"]],
        "Tabel 4.2  Verifikasi Environment Pengembangan pada Mesin Praktikan",
        widths=[3.4, 5.4, 6.2], size=10)

    R.h2("4.2  Inisialisasi Aplikasi dan Root Component")
    R.para("Berkas src/main.js merupakan pintu gerbang aplikasi. Di sinilah "
           "Vue, Pinia, dan Vue Router dipasang pada instance aplikasi "
           "melalui metode app.use(). Perintah app.use(router) inilah yang "
           "mengaktifkan sistem navigasi sisi klien, tanpa perintah tersebut "
           "komponen router-link tidak akan berfungsi.")
    R.code("""import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')""",
           caption="Kode 4.2  Berkas src/main.js")
    R.para("Berkas src/App.vue merupakan root component. Isinya sangat "
           "sederhana, yaitu hanya satu elemen RouterView yang berfungsi "
           "sebagai area dinamis tempat konten halaman disisipkan "
           "otomatis oleh router.")
    R.code("""<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
</template>""",
           caption="Kode 4.3  Berkas src/App.vue")

    R.h2("4.3  Layout dan Outlet")
    R.para("Agar Navbar dan Breadcrumb tidak perlu dipanggil berulang kali "
           "pada setiap halaman, keduanya diletakkan pada berkas layout. "
           "Layout publik memuat Navbar di bagian atas dan "
           "Breadcrumb di atas area konten, sedangkan area konten itu sendiri "
           "berupa router-view yang menjadi tempat halaman anak dirender.")
    R.code("""<script setup>
import Navbar from '@/components/app/Navbar.vue';
import Breadcrumb from '@/components/app/Breadcrumb.vue';
</script>

<template>
  <div class="app-layout">
    <Navbar />
    <main class="main-content">
      <Breadcrumb />
      <router-view />
    </main>
  </div>
</template>""",
           caption="Kode 4.4  Berkas src/layouts/App.vue")

    R.h2("4.4  Pengaturan Rute")
    R.para("Berkas src/router/index.js adalah peta aplikasi. Setiap URL yang "
           "diketik pengguna dicocokkan dengan komponen View yang "
           "berkaitan. Struktur children dipakai untuk membentuk hierarki "
           "Parent–Child, dan setiap rute diberi metadata breadcrumb agar "
           "komponen Breadcrumb dapat membentuk jejak navigasi secara "
           "otomatis.")
    R.code("""const routes = [
  {
    path: '/',
    component: AppLayout,
    children: [
      {
        path: '',
        name: 'home',
        component: () => import('@/views/Home.vue'),
        meta: { breadcrumb: 'Home' }
      },
      {
        path: 'about',
        name: 'about',
        component: () => import('@/views/About.vue'),
        meta: { breadcrumb: 'About' }
      },
      {
        path: 'browse',
        name: 'browse',
        component: () => import('@/views/Browse.vue'),
        meta: { breadcrumb: 'Browse' },
        redirect: '/browse/events',
        children: [
          {
            path: 'events',
            name: 'events',
            component: () => import('@/views/EventList.vue'),
            meta: { breadcrumb: 'Event List' }
          },
          {
            path: 'events/:id',
            name: 'event-detail',
            component: () => import('@/views/EventDetail.vue'),
            meta: { breadcrumb: 'Event Detail' }
          },
          {
            path: 'category',
            name: 'category',
            component: () => import('@/views/Category.vue'),
            meta: { breadcrumb: 'Category' }
          }
        ]
      },
      {
        path: 'contact',
        name: 'contact',
        component: () => import('@/views/Contact.vue'),
        meta: { breadcrumb: 'Contact' }
      }
    ]
  },
  {
    path: '/dashboard',
    component: () => import('@/layouts/DashboardLayout.vue'),
    children: [
      {
        path: '',
        name: 'dashboard-overview',
        component: () => import('@/views/Dashboard.vue'),
        meta: { title: 'Dashboard' }
      },
      {
        path: 'events',
        name: 'dashboard-events',
        component: () => import('@/views/EventManagement.vue')
      }
    ]
  }
]""",
           caption="Kode 4.5  Konfigurasi Rute pada src/router/index.js")
    R.para("Tiga hal penting dapat dibaca langsung dari kode di atas. "
           "Pertama, seluruh komponen view diimpor secara dinamis melalui "
           "fungsi import(), sehingga berkas view tidak diunduh sebelum "
           "dibutuhkan. Kedua, properti redirect pada rute browse "
           "menetapkan arah default ketika pengguna membuka /browse. "
           "Ketiga, rute dengan parameter :id memungkinkan satu komponen "
           "menampilkan banyak entri data berbeda.")

    R.h2("4.5  Komponen Navbar")
    R.para("Navbar merupakan mekanisme transisi. Alih-alih menggunakan tag "
           "a HTML yang memuat ulang halaman, komponen ini memakai "
           "router-link sehingga perpindahan tampilan terjadi secara "
           "instan di sisi klien. Komponen juga menambahkan efek scroll "
           "seperti perubahan background dan blur ketika halaman digulir "
           "melebihi 10 piksel, serta penandaan tautan aktif melalui "
           "pembandingan route.path.")
    R.code("""const menus = [
  { name: 'Home', path: '/' },
  { name: 'About', path: '/about' },
  {
    name: 'Browse',
    path: '/browse',
    children: [
      {
        name: 'Event List',
        path: '/browse/events',
        children: [{ name: 'Event Detail (Sample)', path: '/browse/events/1' }],
      },
      { name: 'Category', path: '/browse/category' },
    ],
  },
  { name: 'Contact', path: '/contact' },
  { name: 'Organizer Dashboard', path: '/dashboard' },
]

const handleScroll = () => {
  isScrolled.value = window.scrollY > 10
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})""",
           caption="Kode 4.6  Potongan Skrip Komponen src/components/app/Navbar.vue")
    R.para("Penandaan tautan aktif dituliskan secara eksplisit agar "
           "halaman utama tetap ditandai aktif ketika pengguna berada pada "
           "root, sekaligus agar tautan Browse tetap ditandai ketika "
           "pengguna berada pada salah satu halamannya.")
    R.code(""":class="{
  active:
    route.path === menu.path ||
    (menu.path !== '/' && route.path.startsWith(menu.path)),
}""",
           caption="Kode 4.7  Logika Penandaan Tautan Aktif pada Navbar.vue")
    R.para("Dropdown dan submenu pada Gambar 4.1 dibentuk sepenuhnya "
           "melalui CSS dengan aturan :hover. Latar dropdown menggunakan "
           "warna abu terang agar kontras dengan navbar berwarna gelap, "
           "sedangkan submenu level kedua muncul di sisi kanan induknya "
           "dengan posisi absolut pada 100 persen dari lebar induk.")
    R.figure("navbar_dropdown.png",
             "Gambar 4.1  Tampilan Dropdown dan Submenu pada Komponen "
             "Navbar.vue", width_cm=12.5)

    R.h2("4.6  Komponen Breadcrumb")
    R.para("Breadcrumb berfungsi sebagai Location Indicator. Komponen ini "
           "menelusuri route.matched untuk memperoleh seluruh rantai rute "
           "yang sedang diakses, mengambil nilai breadcrumb dari metadata "
           "setiap rute, dan menyisipkan butir Home di awal bila belum "
           "present. Untuk rute berparameter, nilai path digantikan dengan "
           "path aktual agar tautan bekerja dengan benar.")
    R.code("""const breadcrumbs = computed(() => {
  const matched = route.matched;
  let crumbs = matched.map((m) => {
    let path = m.path;
    if (path.includes(':')) {
      path = route.path;
    }
    return { name: m.name, path: path, meta: m.meta };
  }).filter(m => m.meta && m.meta.breadcrumb);

  if (route.name === 'event-detail') {
    crumbs.splice(crumbs.length - 1, 0, {
      path: '/browse/events',
      meta: { breadcrumb: 'Event List' }
    });
  }

  if (crumbs.length === 0 || crumbs[0].meta.breadcrumb !== 'Home') {
    crumbs.unshift({ path: '/', meta: { breadcrumb: 'Home' } });
  }

  return crumbs;
});""",
           caption="Kode 4.8  Logika Pembentukan Jejak Breadcrumb")

    R.h2("4.7  Halaman Destinasi Utama dan Lateral")
    R.para("Halaman Home merupakan destinasi utama. Hero section dirancang "
           "agar nilai utama aplikasi berada di area above the fold, "
           "dengan judul berukuran 4rem, teks pendukung 1,25rem, dan satu "
           "tombol aksi utama berwarna kontras. Di bawahnya terdapat "
           "features section dengan tata letak grid adaptif yang secara "
           "otomatis menyesuaikan jumlah kolom sesuai lebar layar.")
    R.figure("home.png",
             "Gambar 4.2  Tampilan Halaman Utama (Home.vue) pada Hero Section",
             width_cm=10.5)
    R.para("Halaman About dan Contact merupakan pergerakan lateral "
           "pada menu Navbar, yaitu halaman yang setara level dengan Home. "
           "Halaman Contact memuat informasi kantor beserta formulir "
           "kontak yang menggunakan event submit.prevent agar halaman "
           "tidak melakukan reload.")
    R.figure("about.png", "Gambar 4.3  Tampilan Halaman About (About.vue)",
             width_cm=10.5)
    R.figure("contact.png",
             "Gambar 4.4  Tampilan Halaman Contact (Contact.vue) beserta "
             "formulir", width_cm=10.5)

    R.h2("4.8  Halaman Browse, Category, dan Event List")
    R.para("Halaman Browse bersifat unik karena merupakan destinasi induk "
           "yang memiliki router-view di dalamnya sendiri. Tugasnya adalah "
           "membungkus halaman-halaman anaknya, yaitu Event List, Event "
           "Detail, dan Category. Halaman ini juga menjadi tempat "
           "redirect default ketika pengguna membuka /browse.")
    R.figure("browse_events.png",
             "Gambar 4.5  Tampilan Halaman Browse (Parent) dan Event List "
             "(Child)", width_cm=10.5)
    R.para("Halaman Event List menampilkan katalog event aktif. Pencarian "
           "dan filter kategori bekerja secara reaktif terhadap computed "
           "filteredEvents, sehingga setiap perubahan input langsung "
           "menyaring kartu tanpa perlu tombol tambahan.")
    R.code("""const filteredEvents = computed(() => {
  return activeEvents.value.filter(event => {
    const q = searchQuery.value.toLowerCase();
    const matchSearch =
      event.title.toLowerCase().includes(q) ||
      event.loc.toLowerCase().includes(q);
    const matchCat =
      selectedCategory.value === 'All' || event.cat === selectedCategory.value;
    return matchSearch && matchCat;
  });
});""",
           caption="Kode 4.9  Logika Pencarian dan Penyaringan Event")
    R.figure("browse_category.png",
             "Gambar 4.6  Tampilan Halaman Category (Category.vue)",
             width_cm=10.5)

    R.h2("4.9  Halaman Detail Event")
    R.para("Halaman EventDetail merupakan ujung destinasi dalam "
           "struktur navigasi. Halaman ini membaca parameter id dari "
           "route.params, mencarinya pada state event, lalu menampilkan "
           "informasi lengkap beserta panel pendaftaran yang menempel "
           "(sticky). Apabila event tidak ditemukan, komponen menampilkan "
           "blok 404 kustom beserta tombol untuk kembali ke katalog.")
    R.figure("event_detail.png",
             "Gambar 4.7  Tampilan Halaman Detail Event (EventDetail.vue)",
             width_cm=10.5)

    R.h2("4.10  Dashboard dan Manajemen Event")
    R.para("Dashboard Organizer menyediakan ringkasan statistik event "
           "dalam bentuk tiga kartu metrik dan satu tabel rekap. "
           "Terdapat pula tombol pintas menuju halaman manajemen event.")
    R.figure("dashboard.png",
             "Gambar 4.8  Tampilan Dashboard Organizer beserta metrik dan "
             "tabel rekap", width_cm=10.5)
    R.para("Halaman Manajemen Event menyediakan tiga tab: Active Events, "
           "Create Event, dan Completed Events. Masing-masing tab mengelola "
           "satu tahap siklus hidup sebuah acara. Formulir pembuatan "
           "memvalidasi keberadaan judul, tanggal, lokasi, dan deskripsi "
           "sebelum data disimpan.")
    R.figure("dashboard_events.png",
             "Gambar 4.9  Tampilan Halaman Manajemen Event "
             "(EventManagement.vue)", width_cm=10.5)
    R.figure("create_event_form.png",
             "Gambar 4.10  Tampilan Formulir Pembuatan Event Baru",
             width_cm=10.5)

    R.h2("4.11  Komponen Reusable dan Modal Konfirmasi")
    R.para("Komponen ui mengemas elemen antarmuka generik agar konsisten "
           "di seluruh aplikasi. AppButton menyediakan dua varian gaya, "
           "AppCard berfungsi sebagai pembungkus dengan slot, sedangkan "
           "AppModal menyediakan dialog konfirmasi dengan efek transisi "
           "opacity, efek blur pada lapisan gelap, serta penutupan otomatis "
           "ketika area di luar dialog diklik.")
    R.code("""<script setup>
defineProps({
  isOpen: { type: Boolean, default: false },
  title: { type: String, default: 'Action Confirmation' },
  message: { type: String, default: 'Are you sure you want to proceed?' },
  confirmText: { type: String, default: 'Yes, Proceed' },
  cancelText: { type: String, default: 'Cancel' }
});
defineEmits(['confirm', 'close']);
</script>

<template>
  <Transition name="modal-fade">
    <div v-if="isOpen" class="modal-overlay" @click.self="$emit('close')">
      <div class="modal-card">
        <div class="modal-header">
          <div class="modal-icon">!</div>
          <h3 class="modal-title">{{ title }}</h3>
        </div>
        <div class="modal-body">
          <p class="modal-message">{{ message }}</p>
          <slot />
        </div>
        <div class="modal-footer">
          <button class="btn-cancel" @click="$emit('close')">{{ cancelText }}</button>
          <button class="btn-confirm" @click="$emit('confirm')">{{ confirmText }}</button>
        </div>
      </div>
    </div>
  </Transition>
</template>""",
           caption="Kode 4.10  Komponen src/components/ui/AppModal.vue")
    R.figure("modal_confirm.png",
             "Gambar 4.11  Tampilan Modal Konfirmasi Aksi pada Komponen "
             "AppModal.vue", width_cm=10.5)

    R.h2("4.12  State Event dan Persistensi")
    R.para("Seluruh data event dikelola pada composable useEvents.js. "
           "Composable ini menyimpan array event pada sebuah ref, kemudian "
           "menyediakan nilai turunan berupa jumlah event, event aktif, dan "
           "event selesai. Setiap mutasi data menggunakan fungsi create, "
           "complete, dan delete yang tersentralisasi sehingga konsisten "
           "di seluruh pemanggil.")
    R.code("""const STORAGE_KEY = 'gatherly_events';

const savedData = localStorage.getItem(STORAGE_KEY);
const events = ref(savedData ? JSON.parse(savedData) : defaultEvents);

watch(
  events,
  (newEvents) => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(newEvents));
  },
  { deep: true }
);

export function useEvents() {
  const totalEvents = computed(() => events.value.length);
  const activeEvents = computed(() => events.value.filter(e => !e.done));
  const completedEvents = computed(() => events.value.filter(e => e.done));

  const createEvent = (eventData) => {
    const newEvent = {
      id: Date.now(),
      title: eventData.title,
      date: eventData.date,
      loc: eventData.loc.startsWith('📍') ? eventData.loc : `📍 ${eventData.loc}`,
      cat: eventData.cat,
      quota: Number(eventData.quota) || 100,
      price: eventData.price || 'Free',
      desc: eventData.desc,
      done: false
    };
    events.value.unshift(newEvent);
    return newEvent;
  };

  const completeEvent = (id) => {
    const target = events.value.find(e => e.id === Number(id));
    if (target) { target.done = true; }
  };

  const deleteEvent = (id) => {
    const index = events.value.findIndex(e => e.id === Number(id));
    if (index !== -1) { events.value.splice(index, 1); }
  };

  const getEventById = (id) =>
    events.value.find(e => e.id === Number(id));

  return { events, totalEvents, activeEvents, completedEvents,
           createEvent, completeEvent, deleteEvent, getEventById };
}""",
           caption="Kode 4.11  Composable src/composables/useEvents.js")

    R.h2("4.13  Sistem Desain Token")
    R.para("Agar tampilan konsisten, proyek memakai custom property CSS "
           "sebagai design token. Token warna, tekstur, dan spasi "
           "didefinisikan satu kali pada src/assets/main.css dan dirujuk "
           "oleh seluruh komponen melalui bentuk var(--nama-token). "
           "Sistem spasi mengadopsi kelipatan delapan piksel agar ritme "
           "vertikal dan horizontal tetap seragam.")
    R.code(""":root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;

  --primary: #6644ff;
  --primary-hover: #5533ee;
  --text-main: #1c1948;
  --text-muted: #666666;
  --text-white: #ffffff;
  --bg-light: #fdfdfd;
  --bg-gray: #f4f4f5;
  --border-color: #e4e4e7;
  --nav-bg: #1c1948;
}""",
           caption="Kode 4.12  Design Token pada src/assets/main.css")

    R.h2("4.14  Ringkasan File Sumber dan Hasil Build")
    R.table(
        ["Folder", "Jumlah Berkas", "Isi Ringkasan"],
        [["src/views/", "10", "Home, About, Contact, Browse, Category, EventList, "
                              "EventDetail, Dasboard (legacy), Dashboard, EventManagement"],
         ["src/components/app/", "2", "Navbar, Breadcrumb"],
         ["src/components/event/", "3", "EventCard, SearchBar, CategoryFilter"],
         ["src/components/ui/", "3", "AppButton, AppCard, AppModal"],
         ["src/layouts/", "2", "App (publik), DashboardLayout (organizer)"],
         ["src/router/", "1", "Tabel rute dan konfigurasi router"],
         ["src/composables/", "1", "useEvents.js"],
         ["src/stores/", "1", "counter.js (Pinia)"],
         ["src/assets/", "3", "base.css, main.css, logo.svg"],
         ["src/ (root)", "2", "main.js, App.vue"]],
        "Tabel 4.3  Perincian File Sumber pada Direktori src/",
        widths=[3.6, 2.0, 9.4], size=9.5)
    R.para("Build produksi dijalankan dengan perintah npm run build. "
           "Proses selesai tanpa galat dalam waktu 404 milidetik dan "
           "menghasilkan 22 berkas hasil build yang terpecah otomatis "
           "berdasarkan rute, seperti pada Tabel 4.4.")
    R.table(
        ["Kelompok Berkas", "Contoh", "Ukuran (gzip)"],
        [["Bundle utama", "index-*.js", "47,57 kB (18,61 kB)"],
         ["Vendor helper", "_plugin-vue_export-helper-*.js", "60,07 kB (23,63 kB)"],
         ["Halaman (JS)", "EventManagement-*.js", "8,99 kB (3,30 kB)"],
         ["Halaman (JS)", "EventList-*.js", "3,34 kB (1,52 kB)"],
         ["Halaman (CSS)", "EventManagement-*.css", "7,23 kB (1,74 kB)"],
         ["Gaya global", "index-*.css", "7,04 kB (2,01 kB)"]],
        "Tabel 4.4  Ringkasan Hasil Build Produksi (npm run build)",
        widths=[4.0, 6.0, 5.0], size=10)


def bab5(R):
    R.h1("BAB V  PENGUJIAN DAN HASIL")

    R.h2("5.1  Strategi Pengujian")
    R.para("Pengujian dilakukan dengan pendekatan black-box terhadap "
           "aplikasi yang sedang berjalan pada development server Vite. "
           "Setiap rute diakses secara langsung melalui alamatnya, kemudian "
           "struktur DOM diperiksa untuk memastikan halaman terender dengan "
           "benar. Untuk pengujian yang bersifat interaktif, seperti "
           "pencarian, filter kategori, publikasi event, dan konfirmasi "
           "modal, aksi dijalankan secara terprogram lalu dampaknya diamati "
           "pada jumlah elemen yang ditampilkan.")
    R.para("Data uji berupa empat event contoh yang diisikan pada "
           "localStorage dengan kunci gatherly_events, yaitu tiga event "
           "aktif dan satu event selesai. Seluruh pengujian dicatat pada "
           "Tabel 5.1.")

    R.h2("5.2  Hasil Pengujian")
    R.table(
        ["Kode", "Skenario Pengujian", "Hasil yang Diharapkan", "Hasil Aktual", "Status"],
        [["TC-01", "Membuka beranda dan memeriksa tautan navigasi",
          "Navbar memuat seluruh menu dan logo aplikasi",
          "8 tautan navigasi terbaca, logo Gatherly tampil, judul hero "
          "terbaca", "Berhasil"],
         ["TC-02", "Membuka /about dan memeriksa penanda menu aktif",
          "Menu About ditandai aktif dan breadcrumb terbentuk",
          "Satu menu aktif (About), breadcrumb “Home / About”", "Berhasil"],
         ["TC-03", "Membuka /browse/events/:id",
          "Breadcrumb menunjukkan empat tingkat navigasi",
          "Breadcrumb “Home / Browse / Event List / Event Detail”, status "
          "Open Registration, harga Rp 350.000", "Berhasil"],
         ["TC-04", "Mengetik “meetup” pada kolom pencarian",
          "Kartu event tersaring sesuai kata kunci",
          "Jumlah kartu turun dari 3 menjadi 1, namely “Tech Meetup: "
          "Scaling Frontend Architecture”; setelah dikosongkan kembali "
          "menjadi 3", "Berhasil"],
         ["TC-05", "Memilih kategori “Workshop”",
          "Hanya event berkategori Workshop yang tampil",
          "Jumlah kartu turun dari 3 menjadi 1 dengan label WORKSHOP",
          "Berhasil"],
         ["TC-06", "Mengakses /browse/events/999999",
          "Halaman 404 kustom tampil",
          "Blok “404 - Event Not Found” beserta tombol kembali tampil",
          "Berhasil"],
         ["TC-07", "Membuka /dashboard",
          "Metrik dan tabel rekap sesuai jumlah data",
          "Total Events 4, Active Events 3, Completed Events 1, tabel "
          "memuat 4 baris", "Berhasil"],
         ["TC-08", "Memeriksa persistensi state",
          "Data event tersimpan pada localStorage",
          "Kunci gatherly_events berisi 4 event, 1 di antaranya berstatus "
          "done", "Berhasil"],
         ["TC-09", "Memeriksa perilaku Navbar saat digulir",
          "Navbar melekat di atas dan menu tetap rapi",
          "position: sticky dengan top 0 px, nav-menu display flex "
          "gap 40 px", "Berhasil"],
         ["TC-10", "Mempublish event baru melalui formulir",
          "Event tersimpan dan katalog publik bertambah",
          "Alert “Event published successfully and is now live!” tampil, "
          "jumlah data pada storage menjadi 5", "Berhasil"],
         ["TC-11", "Memastikan event baru tampil di katalog publik",
          "Event baru muncul pada daftar",
          "Empat kartu tampil dengan “Uji Otomatis Praktikum” di posisi "
          "teratas", "Berhasil"],
         ["TC-12", "Mengirim formulir tanpa mengisi kolom wajib",
          "Validasi menampilkan pesan galat",
          "Alert “Please fill in all required fields before publishing the "
          "event!” tampil dan data tidak bertambah", "Berhasil"],
         ["TC-13", "Memilih tombol Complete Event",
          "Modal konfirmasi tampil sebelum tindakan dijalankan",
          "Modal menampilkan judul “Complete Event?” beserta nama event "
          "yang dituju", "Berhasil"],
         ["TC-14", "Menjalankan build produksi",
          "Build selesai tanpa galat",
          "npm run build selesai dalam 404 ms, 22 berkas hasil build "
          "terbentuk", "Berhasil"]],
        "Tabel 5.1  Hasil Pengujian Black-Box Fungsional",
        widths=[1.3, 3.4, 3.4, 4.4, 1.6], size=9)

    R.h2("5.3  Pembahasan Hasil Pengujian")
    R.para("Seluruh empat belas skenario pengujian menghasilkan status "
           "berhasil, sehingga tidak ditemukan cacat fungsional pada "
           "cakupan Modul 0 dan Modul 1. Beberapa temuan perlu dicatat "
           "sebagai berikut.")
    for x in [
        "Mekanisme hierarki Parent–Child bekerja konsisten. Rute /browse/events/:id "
        "menghasilkan breadcrumb empat tingkat tanpa perlu konfigurasi "
        "tambahan pada setiap halaman, karena komponen Breadcrumb hanya "
        "bergantung pada route.matched dan metadata rute.",
        "Rasio kode pada View menjadi sangat kecil. Halaman EventList hanya "
        "sekitar 40 baris, sedangkan logika penyaringan, pemformatan "
        "tanggal, dan navigasi detail dipindahkan ke composable maupun "
        "komponen turunan.",
        "Filter dan pencarian bekerja reaktif tanpa perlu tombol tambahan. "
        "Hal tersembunyi karena nilai pencarian dan kategori disimpan "
        "pada ref, sementara hasil penyaringan dihitung oleh computed.",
        "Validasi formulir masih pada tataran antarmuka. Pesan galat "
        "ditampilkan melalui alert box di dalam halaman, bukan melalui "
        "validasi sisi server, sehingga masih ada ruang perbaikan pada "
        "modul lanjutan.",
        "Modal konfirmasi berjalan seperti yang dirancang, termasuk "
        "penutupan otomatis ketika area di luar dialog diklik.",
    ]:
        R.bullet(x)

    R.h2("5.4  Verifikasi Kesesuaian dengan Capaian Pembelajaran")
    R.table(
        ["No", "Capaian Pembelajaran Mata Kuliah", "Bukti Implementasi", "Status"],
        [["1", "Memahami relasi Site Map, View, dan Router",
          "Peta Situs pada Gambar 3.1 dan Tabel Rute 3.4", "Terpenuhi"],
         ["2", "Menerapkan hierarki Parent–Child",
          "Properti children pada src/router/index.js dan pengujian TC-03",
          "Terpenuhi"],
         ["3", "Mengimplementasikan pola pergerakan pengguna",
          "Transisi router-link dan tombol kembali pada EventDetail.vue",
          "Terpenuhi"],
         ["4", "Merancang Navbar interaktif berbasis router-link",
          "Komponen Navbar.vue beserta dropdown dua tingkat pada Gambar 4.1",
          "Terpenuhi"],
         ["5", "Merancang Location Indicator (Breadcrumb)",
          "Komponen Breadcrumb.vue dan pengujian TC-02 serta TC-03",
          "Terpenuhi"],
         ["6", "Menjalankan aplikasi Vue utuh dengan berbagai halaman",
          "Sembilan rute aktif dan 22 berkas hasil build pada Tabel 4.4",
          "Terpenuhi"],
         ["7", "Menyiapkan environment dan mengonfigurasi project Vue.js",
          "Rangkaian perintah pada Kode 4.1 dan verifikasi Tabel 4.2",
          "Terpenuhi"]],
        "Tabel 5.2  Pencapaian Capaian Pembelajaran Mata Kuliah",
        widths=[1.0, 4.8, 6.8, 2.4], size=9.5)


def bab6(R):
    R.h1("BAB VI  KESIMPULAN DAN SARAN")

    R.h2("6.1  Kesimpulan")
    R.para("Berdasarkan hasil implementasi dan pengujian, laporan ini "
           "dapat menyimpulkan beberapa hal sebagai berikut.")
    for x in [
        "Persiapan environment pada Modul 0 berhasilyelexecute dengan "
        "lengkap. Visual Studio Code, Node.js v22.15.1, npm 10.9.2, dan "
        "ekstensi Vue (Official) terpasang dengan benar, generator "
        "create-vue berhasil membentuk kerangka project belajar-vue, dan "
        "development server Vite dapat dijalankan serta dihentikan melalui "
        "npm run dev dan Ctrl + C.",
        "Konsep Site Map berhasil diterjemahkan menjadi hierarki rute "
        "Parent–Child pada src/router/index.js. Sembilan rute aktif "
        "terdaftar, dengan Browse sebagai Destinasi Induk dan Event Detail "
        "sebagai ujung destinasi berparameter.",
        "Komponen Navbar dan Breadcrumb berhasil dirancang sesuai "
        "konsep transisi dan orientasi. Pengujian TC-01 sampai TC-03 "
        "membuktikan bahwa penandaan menu aktif dan pembentukan jejak "
        "navigasi bekerja otomatis pada setiap tingkat kedalaman rute.",
        "Struktur aplikasi yang terpisah antara layout, views, dan "
        "components menghasilkan basis kode yang ringkas dan mudah "
        "dikembangkan. Sembilan halaman yang masing-masing hanya "
        "tersusun atas beberapa ratus baris kode, sementara logika utama "
        "berada pada composable useEvents.js.",
        "Seluruh 14 skenario pengujian black-box berhasil dilalui dan "
        "build produksi selesai tanpa galat dalam waktu 404 milidetik, "
        "sehingga aplikasi memenuhi capaian pembelajaran Modul 0 dan "
        "Modul 1.",
    ]:
        R.bullet(x)

    R.h2("6.2  Saran")
    for x in [
        "Validasi formulir sebaiknya dipindahkan ke lapisan composable "
        "atau modul validasi terpisah agar dapat dipakai ulang pada "
        "seluruh formulir, bukan hanya pada halaman manajemen event.",
        "Data event yang masih bergantung pada localStorage sebaiknya "
        "dipindahkan ke API backend agar dapat diakses lintas perangkat "
        "dan oleh banyak pengguna secara bersamaan.",
        "Pengujian otomatis dengan Vitest dan Playwright perlu "
        "ditambahkan pada modul lanjutan agar verifikasi reaktivitas dan "
        "alur navigasi tidak bergantung pada pemeriksaan manual.",
        "Halaman About dan Category saat ini masih memakai data contoh "
        "statis. Keduanya dapat disambungkan dengan state yang sama "
        "seperti EventList agar seluruh aplikasi benar-benar konsisten.",
        "Aset ikon yang masih berupa karakter teks pada beberapa "
        "komponen sebaiknya diganti dengan pustaka ikon vektor agar "
        "konsistensi visual lebih terjaga.",
    ]:
        R.bullet(x)


def back_matter(R):
    R.h1("DAFTAR PUSTAKA")
    refs = [
        "Vue.js. (2024). Vue.js Documentation: The Progressive JavaScript "
        "Framework. Diambil dari https://vuejs.org/guide/ pada 2026.",
        "Vue Router. (2024). Vue Router Documentation: Official Router for "
        "Vue.js. Diambil dari https://router.vuejs.org/ pada 2026.",
        "Vite. (2024). Vite Guide: Getting Started and Build Tool "
        "Configuration. Diambil dari https://vite.dev/guide/ pada 2026.",
        "Vue.js. (2024). Vue.js Composition API FAQ. Diambil dari "
        "https://vuejs.org/guide/extras/composition-api-faq.html pada 2026.",
        "Mozilla Developer Network. (2024). Using Web Storage. Diambil dari "
        "https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage "
        "pada 2026.",
        "Mozilla Developer Network. (2024). CSS Grid Layout. Diambil dari "
        "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout pada "
        "2026.",
        "Tim Asisten Praktikum. (2026). Modul Praktikum: Modul 0 dan Modul 1 "
        "Pengembangan UI Lanjut. Program Studi Sistem Informasi, Fakultas "
        "Rekayasa Industri, Universitas Telkom.",
        "OpenCode. (2026). Dokumentasi Resmi OpenCode. Diambil dari "
        "https://opencode.ai/docs/ pada 2026.",
    ]
    for i, r in enumerate(refs, 1):
        R.para("[%d] %s" % (i, r), size=11, align="left", indent=0,
               space_after=8, line=1.3, left_indent=1.0)

    R.h1("LAMPIRAN")
    R.h2("Lampiran A  Perintah Terminal yang Digunakan")
    R.code("""# Verifikasi environment
node -v
npm -v

# Membuat kerangka project
npm create vue@latest

# Masuk ke direktori project dan mengunduh dependensi
cd belajar-vue
npm install

# Merapikan format kode
npm run format

# Menjalankan development server
npm run dev
# Alamat: http://localhost:5173/

# Menghentikan development server
Ctrl + C

# Build produksi
npm run build

# Pratinjau hasil build
npm run preview""",
           caption="Kode A.1  Ringkasan Perintah Terminal pada Praktikum")

    R.h2("Lampiran B  Berkas package.json")
    R.code("""{
  "name": "belajar-vue",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "format": "prettier --write --experimental-cli src/"
  },
  "dependencies": {
    "pinia": "^4.0.3",
    "vue": "^3.5.42",
    "vue-router": "^5.3.1"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^6.0.8",
    "prettier": "3.9.6",
    "vite": "^8.2.2",
    "vite-plugin-vue-devtools": "^8.2.1"
  },
  "engines": {
    "node": "^22.18.0 || >=24.12.0"
  }
}""",
           caption="Kode B.1  Manifest package.json Proyek belajar-vue")

    R.h2("Lampiran C  Konfigurasi Editor dan Format Kode")
    R.code("""// .prettierrc.json
{
  "$schema": "https://json.schemastore.org/prettierrc",
  "semi": false,
  "singleQuote": true,
  "printWidth": 100
}

// jsconfig.json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "exclude": ["node_modules", "dist"]
}

// vite.config.js
export default defineConfig({
  plugins: [vue(), vueDevTools()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})""",
           caption="Kode C.1  Konfigurasi Prettier, Alias Path, dan Vite")
