<script setup>
import { ref } from 'vue'
import consumerApi from '../api/consumer.js'

import tasks from '../components/tasks.vue'

</script>

<template>
  <main>
    <img src="/logo_dark.png" alt="Fábrica de Software" class="logo">
    <tasks/>
  </main>
</template>


<style scoped>

.logo {
        position: absolute;
        left: 1%;
        top: 1%;
        width: 50px;
    }

    main {
        position: relative;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #22272e;
    }

.mode {
        position: absolute;
        right: 1%;
        top: 1%;
        width: 20px;
        cursor: pointer;
    }

</style>