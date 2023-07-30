<script setup>
import Form from '../components/Form.vue';
import { ref } from 'vue';

const darkMode = ref(true);

const toggleDarkMode = () => {
    darkMode.value = !darkMode.value;
}
</script>

<template>
    <main :class="darkMode ? 'dark' : ''">
        <img :src="darkMode ? '/logo_dark.png' : '/logo_white.png'" alt="Logo" class="logo">
        <Form :darkMode="darkMode"/>

        <img @click="toggleDarkMode" :src="darkMode ? '/sun.svg' : '/moon.svg'" alt="" class="mode">
    </main>
</template>

<style scoped>
    main {
        position: relative;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #f1f1f1;
    }

    .logo {
        position: absolute;
        left: 1%;
        top: 1%;
        width: 50px;
    }

    .mode {
        position: absolute;
        right: 1%;
        top: 1%;
        width: 20px;
        cursor: pointer;
    }

    .dark {
        background-color: #22272e;
    }
</style>