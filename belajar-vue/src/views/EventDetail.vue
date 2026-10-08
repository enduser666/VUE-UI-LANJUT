<script setup>
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
</script>

<template>
  <div class="event-detail-page">
    <button @click="router.push('/browse/events')" class="btn-back">
      &larr; Back to Events
    </button>

    <!-- DETAIL HEADER -->
    <div class="detail-header">
      <span class="event-tag">Workshop & Training</span>
      <h1>Vue.js Mastery Workshop {{ route.params.id }}</h1>
      <div class="meta-info">
        <span class="meta-item">📅 October 12, 2026</span>
        <span class="meta-item">📍 Tech Hub, Jakarta Pusat</span>
        <span class="meta-item">👥 Quota: 150 Attendees</span>
      </div>
    </div>

    <!-- ASYMMETRICAL CONTENT (2fr : 1fr) -->
    <div class="detail-content grid-asymmetric">
      <!-- MAIN DESCRIPTION (F-PATTERN) -->
      <div class="main-desc">
        <h2>About This Event</h2>
        <p>
          Bergabunglah dalam workshop pelatihan pengembangan web interface terbesar tahun ini, sebuah kolaborasi Gatherly dengan komunitas developer terkemuka. Acara ini dirancang secara komprehensif bagi praktisi front-end yang ingin memperdalam penguasaan teknologi web modern.
        </p>
        <p>
          Kita akan membedah tantangan industri riil, arsitektur Single Page Application (SPA), serta praktik implementasi Layout System berstandar industri dengan prioritas utama pada visual hierarchy dan pengalaman pengguna yang responsif.
        </p>

        <h2>Event Agenda</h2>
        <ul class="agenda-list">
          <li><strong>09:00 AM</strong> Registration & QR Check-in Scanning</li>
          <li><strong>10:00 AM</strong> Session 1: Vue Router & Navigation Fundamentals</li>
          <li><strong>11:30 AM</strong> Coffee Break & Networking Session</li>
          <li><strong>01:00 PM</strong> Session 2: Layout System & Grid Implementation</li>
          <li><strong>03:00 PM</strong> Q&A & Closing Remarks</li>
        </ul>
      </div>

      <!-- SIDEBAR (FOCAL POINT & STICKY PANE) -->
      <div class="sidebar">
        <div class="ticket-card sticky-pane">
          <h3>Attendee Registration</h3>
          <p class="price">Free</p>
          <p class="ticket-desc">Secure your seat now before the quota is full.</p>
          <button class="btn-register">Register Now</button>
          <p class="spots">Only 12 seats left!</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* ==========================================================================
   BACK BUTTON
   ========================================================================== */
.btn-back {
  background: none;
  border: none;
  font-size: 1rem;
  cursor: pointer;
  margin-bottom: var(--space-6);
  color: var(--text-muted);
  padding: 0;
  display: inline-flex;
  align-items: center;
  transition: color 0.2s;
}

.btn-back:hover {
  color: var(--primary);
}

/* ==========================================================================
   DETAIL HEADER
   ========================================================================== */
.detail-header {
  background: var(--bg-light);
  border-radius: var(--space-4);
  border: 1px solid var(--border-color);
  padding: var(--space-12) var(--space-8);
  margin-bottom: var(--space-8);
}

.event-tag {
  display: inline-block;
  background: rgba(102, 68, 255, 0.1);
  color: var(--primary);
  padding: var(--space-1) var(--space-4);
  border-radius: 50px;
  font-weight: 600;
  font-size: 0.9rem;
  margin-bottom: var(--space-4);
}

h1 {
  font-size: 2.8rem;
  margin: 0 0 var(--space-4) 0;
  line-height: 1.2;
  color: var(--text-main);
}

.meta-info {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-6);
}

.meta-item {
  color: var(--text-muted);
  font-weight: 500;
  font-size: 1.05rem;
}

/* ==========================================================================
   ASYMMETRICAL LAYOUT (2fr : 1fr):
   Rasio asimetris 8:4 (66.6% konten vs 33.3% sidebar konversi) untuk
   mengarahkan bobot visual utama ke penjelasan materi event sekaligus
   menjaga panel aksi selalu mudah dijangkau.
   ========================================================================== */
.grid-asymmetric {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: var(--space-12);
}

@media (max-width: 900px) {
  .grid-asymmetric {
    grid-template-columns: 1fr;
    gap: var(--space-8);
  }
}

/* ==========================================================================
   F-PATTERN:
   Konten editorial diatur agar mata memindai secara horizontal pada
   subheading (dengan aksen border-left primary) dan awal baris agenda
   (dengan penanda waktu tebal di sisi kiri) sebelum bergerak vertikal.
   ========================================================================== */
.main-desc h2 {
  margin: 0 0 var(--space-4) 0;
  font-size: 1.8rem;
  color: var(--text-main);
  border-left: 4px solid var(--primary);
  padding-left: var(--space-2);
}

.main-desc p {
  line-height: 1.8;
  margin: 0 0 var(--space-6) 0;
  font-size: 1.05rem;
  color: var(--text-main);
}

.agenda-list {
  list-style: none;
  padding: 0;
  margin: 0 0 var(--space-8) 0;
}

.agenda-list li {
  padding: var(--space-3) 0;
  border-bottom: 1px solid var(--border-color);
  color: var(--text-muted);
  font-size: 1.05rem;
}

.agenda-list li strong {
  color: var(--text-main);
  margin-right: var(--space-2);
}

/* ==========================================================================
   FOCAL POINT & SQUINT TEST:
   .ticket-card dan .btn-register didesain menjadi elemen paling mencolok
   di sisi kanan halaman. Warna primer kontras tinggi dan harga tebal
   memastikan fokus konversi tetap dominan dalam uji squint test.
   ========================================================================== */
.ticket-card {
  background: #ffffff;
  padding: var(--space-8);
  border-radius: var(--space-4);
  border: 1px solid var(--border-color);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.06);
  text-align: center;
}

.ticket-card h3 {
  font-size: 1.5rem;
  margin: 0 0 var(--space-2) 0;
  color: var(--text-main);
}

.price {
  font-size: 2.8rem;
  font-weight: 800;
  color: var(--primary);
  margin: 0 0 var(--space-2) 0;
}

.ticket-desc {
  color: var(--text-muted);
  margin: 0 0 var(--space-6) 0;
  line-height: 1.5;
}

.btn-register {
  width: 100%;
  padding: var(--space-4);
  background: var(--primary);
  color: #ffffff;
  border: none;
  border-radius: 12px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s, transform 0.2s;
  box-shadow: 0 4px 15px rgba(102, 68, 255, 0.3);
}

.btn-register:hover {
  background: var(--primary-hover);
  transform: translateY(-2px);
}

.spots {
  margin-top: var(--space-4);
  margin-bottom: 0;
  color: #e63946;
  font-weight: 600;
  font-size: 0.95rem;
}

/* ==========================================================================
   STICKY PANE:
   Membuat panel tiket tetap menempel di viewport atas (top: 100px) saat
   pengguna menggulir (scroll) membaca detail deskripsi dan agenda yang panjang.
   ========================================================================== */
.sticky-pane {
  position: sticky;
  top: 100px;
}
</style>
