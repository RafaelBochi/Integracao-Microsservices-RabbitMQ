<script setup>
import { onMounted, computed, ref } from 'vue';
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();

onMounted(
  ()=> {
    userStore.getUsers();
  }
)
</script>

<template>
  <RouterView />
</template>

<style scoped>

</style>
