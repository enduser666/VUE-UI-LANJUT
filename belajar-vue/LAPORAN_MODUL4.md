# Laporan Modul 4 – Manajemen State dan Interaksi Pengguna (Gatherly)

## A. File yang dibuat/diubah
### Baru
- `src/composables/useEvents.js`
- `src/components/ui/AppModal.vue`
- `src/components/ui/AppCard.vue`
- `src/components/ui/AppButton.vue`
- `src/components/event/EventCard.vue`
- `src/components/event/SearchBar.vue`
- `src/components/event/CategoryFilter.vue`
- `src/views/EventManagement.vue`

### Diubah
- `src/views/Dashboard.vue`
- `src/views/EventList.vue`
- `src/views/EventDetail.vue`
- `src/layouts/DashboardLayout.vue`
- `src/router/index.js`
- `src/assets/main.css`

## B. Penyesuaian komponen existing
- `AppCard`: wrapper dengan satu root element + `<slot />` agar `class` parent menempel (fallthrough attrs).
- `AppButton`: mendukung `variant` (`primary`/`secondary`), meneruskan `type`, `disabled`, dan `@click` ke `<button>`.
- `EventCard`: membaca field skema baru (`loc`, `cat`, `done`, dll.) dan emit `view-detail` dengan payload `event.id`.
- `SearchBar` dan `CategoryFilter`: mendukung `v-model` (`modelValue`/`update:modelValue`); `CategoryFilter` menerima prop `categories`.
- `main.css`: hanya menambahkan `--space-5: 20px`; nilai existing tidak ditimpa.

## C. Hasil build/lint dan verifikasi
- `npm run build`: sukses (64 modules, tanpa error).
- Tidak ada skrip `lint`; skrip yang tersedia hanya `format` (prettier), tidak dijalankan agar diff tetap terfokus.
- Checklist verifikasi (logika dicek via review kode):
  - [x] Empty state awal (`/browse/events`, `/dashboard`)
  - [x] Validasi field kosong (alert merah)
  - [x] Create event + reset form + auto pindah tab
  - [x] Sinkronisasi Dashboard/Browse/LocalStorage
  - [x] Detail dinamis + 404
  - [x] Modal Complete (blur 8px, close on overlay click)
  - [x] Complete -> Completed tab, hilang dari Browse, status di Detail
  - [x] Modal Delete + penghapusan total
  - [x] Sidebar dual-active bug diperbaiki
  - [x] Filter pencarian & kategori
  - [x] Tidak ada manipulasi DOM manual

## D. Catatan
- Repo root berada di `C:\Users\HP\Documents\P UI 2`; proyek di subfolder `belajar-vue`.
- Branch kerja: `Modul-4`.
- `src/views/Dasboard.vue` lama dibiarkan (tidak dipakai) karena router kini mengarah ke `Dashboard.vue`.
- `gh` CLI tidak tersedia, sehingga branch hanya ter-commit lokal.
