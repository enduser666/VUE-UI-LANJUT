<script setup>
defineProps({
  categories: { type: Array, default: () => [] },
  modelValue: { type: String, default: 'All' }
});
const emit = defineEmits(['update:modelValue']);
</script>

<template>
  <select
    :value="modelValue"
    @change="$emit('update:modelValue', $event.target.value)"
    class="category-filter"
  >
    <option v-for="cat in categories" :key="cat" :value="cat">{{ cat }}</option>
  </select>
</template>

<style scoped>
.category-filter {
  padding: var(--space-3) var(--space-4);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  font-size: 1rem;
  outline: none;
  background: white;
  cursor: pointer;
}
.category-filter:focus {
  border-color: var(--primary);
}
</style>
