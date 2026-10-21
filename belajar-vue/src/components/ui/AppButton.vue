<script setup>
defineProps({
  variant: { type: String, default: 'primary' }
});
</script>

<template>
  <button :class="['app-btn', `app-btn--${variant}`]">
    <slot />
  </button>
</template>

<style scoped>
.app-btn {
  padding: var(--space-3) var(--space-6);
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  border: none;
  transition: all 0.2s;
}
.app-btn--primary {
  background: var(--primary);
  color: #ffffff;
}
.app-btn--primary:hover {
  background: var(--primary-hover);
}
.app-btn--secondary {
  background: var(--bg-light);
  color: var(--text-muted);
  border: 1px solid var(--border-color);
}
.app-btn--secondary:hover {
  background: #e9ecef;
  color: var(--text-main);
}
.app-btn:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}
</style>
