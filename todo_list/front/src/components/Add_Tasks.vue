<script setup>

import { ref, inject } from 'vue'

const closeModal = inject('closeModal');

const callCloseModal = () => {
    closeModal()
}

</script>

<template>

    <section class="add-task">
        <div class="content">
            asdsadadsad
        </div>
        <button @click="callCloseModal">
            X
        </button>
    </section>

</template>

<style>

</style>