<script setup>
/* DASHBOARD OVERVIEW */
</script>

<template>
  <div class="dashboard-overview">
    <h2>Welcome back, Organizer</h2>

    <!-- METRICS GRID (DATA DENSITY) -->
    <div class="metrics-grid">
      <div class="metric-card">
        <h3>Total Tickets Sold</h3>
        <p class="metric-value">1,245</p>
      </div>

      <div class="metric-card">
        <h3>Page Views</h3>
        <p class="metric-value">8,302</p>
      </div>

      <div class="metric-card">
        <h3>Revenue</h3>
        <p class="metric-value">$12,450</p>
      </div>
    </div>

    <!-- DATA TABLE CONTAINER (DATA DENSITY) -->
    <div class="data-table-container">
      <h3>Recent Registrations</h3>
      <table class="data-table">
        <thead>
          <tr>
            <th>Attendee Name</th>
            <th>Event</th>
            <th>Registration Date</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="i in 5" :key="i">
            <td>John Doe {{ i }}</td>
            <td>Community Gathering {{ i }}</td>
            <td>Oct 1{{ i }}, 2026</td>
            <td>
              <span class="status-badge">Confirmed</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
/* ==========================================================================
   DASHBOARD OVERVIEW & DATA DENSITY:
   - Data Density menyajikan ringkasan metrik performa operasional tingkat tinggi
     dalam card modular yang ringkas.
   - Tabel registrant dirancang dengan padding optimal (base-8: var(--space-3)
     var(--space-4)) untuk memaksimalkan jumlah baris terbaca sekaligus menjaga
     ruang nafas tipografis.
   ========================================================================== */
.dashboard-overview h2 {
  font-size: 1.8rem;
  color: var(--text-main);
  margin: 0 0 var(--space-6) 0;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--space-6);
  margin-bottom: var(--space-8);
}

.metric-card {
  background: #ffffff;
  padding: var(--space-6);
  border-radius: var(--space-3);
  border: 1px solid var(--border-color);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
}

.metric-card h3 {
  font-size: 1rem;
  color: var(--text-muted);
  margin: 0 0 var(--space-2) 0;
  font-weight: 500;
}

.metric-value {
  font-size: 2.2rem;
  font-weight: 700;
  color: var(--primary);
  margin: 0;
}

.data-table-container {
  background: #ffffff;
  padding: var(--space-6);
  border-radius: var(--space-3);
  border: 1px solid var(--border-color);
  overflow-x: auto;
}

.data-table-container h3 {
  font-size: 1.25rem;
  color: var(--text-main);
  margin: 0 0 var(--space-4) 0;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: var(--space-3) var(--space-4);
  text-align: left;
  border-bottom: 1px solid var(--border-color);
}

th {
  background: var(--bg-gray);
  color: var(--text-muted);
  font-weight: 600;
  font-size: 0.9rem;
}

td {
  color: var(--text-main);
  font-size: 0.95rem;
}

.status-badge {
  background: rgba(46, 204, 113, 0.1);
  color: #2ecc71;
  padding: var(--space-1) var(--space-2);
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 600;
  display: inline-block;
}
</style>
