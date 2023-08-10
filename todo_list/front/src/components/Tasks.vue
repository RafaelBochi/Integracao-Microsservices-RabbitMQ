<script setup>
import { computed, ref } from 'vue'


</script>

<template>
    <section>
        <h2>Tasks</h2>
        <div class="tasks">
        </div>
    </section>
</template>

<style>
section {
    position: relative;
    width: 40%;
    height: 50%;
    background: #ff8b3f;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 2%;
    border-radius: 10px;
}

h2 {
    font-size: 2rem;
    margin-bottom: 2%;
    color: #f1f1f1;
    font-weight: bolder;
}
</style>