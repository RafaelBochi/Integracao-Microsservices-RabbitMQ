<script setup>
import { onMounted } from 'vue';
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
