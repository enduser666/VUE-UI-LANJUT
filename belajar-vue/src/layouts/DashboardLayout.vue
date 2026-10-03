<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<template>
  <!-- RAIL & PANE SYSTEM -->
  <div class="dashboard-layout">
    <!-- ASIDE: DASHBOARD RAIL (LOCKED SIDEBAR) -->
    <aside class="dashboard-rail">
      <div class="rail-brand">
        <router-link to="/">Gatherly Organizer</router-link>
      </div>

      <nav class="rail-nav">
        <router-link to="/dashboard" class="rail-link" exact-active-class="active">
          Overview
        </router-link>
        <a href="#" class="rail-link" @click.prevent>My Events</a>
        <a href="#" class="rail-link" @click.prevent>Attendees</a>
        <a href="#" class="rail-link" @click.prevent>QR Check-in</a>
      </nav>

      <div class="rail-footer">
        <router-link to="/" class="rail-link">
          &larr; Back to Public
        </router-link>
      </div>
    </aside>

    <!-- MAIN: DASHBOARD PANE (INDEPENDENT SCROLL) -->
    <main class="dashboard-pane">
      <header class="pane-header">
        <h1>Dashboard</h1>
        <div class="user-profile">Admin</div>
      </header>

      <div class="pane-content">
        <RouterView />
      </div>
    </main>
  </div>
</template>

<style scoped>
/* ==========================================================================
   RAIL & PANE SYSTEM:
   - Dashboard rail (sidebar 260px) terkunci diam (non-scrollable) di sisi kiri.
   - Dashboard pane (konten utama) memiliki overflow-y: auto untuk scroll mandiri.
   - Root dashboard-layout memiliki height: 100vh dan overflow: hidden sehingga
     window browser tidak pernah memicu scrollbar ganda.
   ========================================================================== */
.dashboard-layout {
  display: flex;
  height: 100vh;
  overflow: hidden;
  background: var(--bg-gray);
}

.dashboard-rail {
  width: 260px;
  background: #1c1948;
  color: #ffffff;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  height: 100%;
}

.rail-brand {
  padding: var(--space-6);
  font-size: 1.2rem;
  font-weight: 700;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.rail-brand a {
  color: #ffffff;
  text-decoration: none;
}

.rail-nav {
  flex: 1;
  padding: var(--space-6) 0;
  display: flex;
  flex-direction: column;
}

.rail-link {
  padding: var(--space-3) var(--space-6);
  color: #a0a0b0;
  text-decoration: none;
  font-weight: 500;
  transition: background-color 0.2s, color 0.2s, border-left-color 0.2s;
  display: block;
  border-left: 4px solid transparent;
}

.rail-link:hover,
.rail-link.active,
.rail-link.router-link-exact-active {
  background: rgba(255, 255, 255, 0.05);
  color: #ffffff;
  border-left: 4px solid var(--primary);
}

.rail-footer {
  padding: var(--space-6);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.rail-footer .rail-link {
  padding: 0;
  border-left: none;
}

.dashboard-pane {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  height: 100%;
}

.pane-header {
  background: #ffffff;
  padding: var(--space-4) var(--space-8);
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border-color);
  position: sticky;
  top: 0;
  z-index: 10;
}

.pane-header h1 {
  font-size: 1.5rem;
  margin: 0;
  color: var(--text-main);
}

.user-profile {
  font-weight: 600;
  color: var(--text-main);
  background: var(--bg-gray);
  padding: var(--space-1) var(--space-3);
  border-radius: 6px;
  font-size: 0.9rem;
}

.pane-content {
  padding: var(--space-8);
}
</style>
