<script setup>
defineProps({
  event: { type: Object, required: true }
});
const emit = defineEmits(['view-detail']);
</script>

<template>
  <div class="event-card">
    <div class="event-body">
      <div class="event-meta">
        <span class="event-date">{{ event.date }}</span>
        <span class="event-category">{{ event.cat }}</span>
      </div>
      <h3 class="event-title">{{ event.title }}</h3>
      <p class="event-loc">{{ event.loc }}</p>
      <p class="event-desc">{{ event.desc }}</p>
      <div class="card-footer">
        <button class="btn-link" @click="$emit('view-detail', event.id)">View Event Details &rarr;</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.event-card {
  background: #ffffff;
  border-radius: var(--space-4);
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
  display: flex;
  flex-direction: column;
  transition: transform 0.2s, box-shadow 0.2s;
}
.event-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 25px rgba(0, 0, 0, 0.06);
}
.event-body {
  padding: var(--space-6);
  display: flex;
  flex-direction: column;
  height: 100%;
}
.event-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-4);
}
.event-date {
  background: rgba(102, 68, 255, 0.1);
  color: var(--primary);
  padding: var(--space-1) var(--space-2);
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.85rem;
}
.event-category {
  color: var(--text-muted);
  font-size: 0.85rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.event-title {
  font-size: 1.4rem;
  color: var(--text-main);
  margin: 0 0 var(--space-2) 0;
}
.event-loc {
  color: var(--text-muted);
  font-size: 0.95rem;
  margin: 0 0 var(--space-4) 0;
}
.event-desc {
  color: var(--text-muted);
  line-height: 1.6;
  font-size: 0.95rem;
  margin: 0 0 var(--space-6) 0;
  flex-grow: 1;
}
.card-footer {
  border-top: 1px solid var(--border-color);
  padding-top: var(--space-4);
}
.btn-link {
  background: none;
  border: none;
  display: inline-block;
  color: var(--text-main);
  font-weight: 600;
  cursor: pointer;
  transition: color 0.2s;
}
.btn-link:hover {
  color: var(--primary);
}
</style>
