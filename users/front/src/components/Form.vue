<script setup>
import { computed } from "vue";

const props = defineProps({
    darkMode: Boolean
});

const darkMode = computed(() => props.darkMode);
</script>

<template>
    <section :class="darkMode ? 'dark' : ''">
        <h2>
            Adicionar Usuario
        </h2>

        <div class="inputs">
            <div class="inputName">
                <input type="text" required>
                <label>Username</label>
                <i></i>
            </div>

            <div class="inputEmail">
                <input type="text" required>
                <label>Email</label>
                <i></i>
            </div>

            <div class="inputPassword">
                <input type="password" required>
                <label>Password</label>
                <i></i>
            </div>
        </div>

        <button>
            Criar Usuario
        </button>
    </section>
</template>

<style scoped>
    section {
        position: relative;
        width: 20%;
        height: 50%;
        background: #267a7a ;
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
        color: #22272e;
        font-weight: bolder;
    }

    .inputs {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
        width: 100%;
        gap: 20px;
    }

    .inputs > div {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 90%;
    }

    .inputs > div > input {
        width: 100%;
        height: 30px;
        border: none;
        border-bottom: 1px solid #22272e;
        background: #22272e;
        color: #bbc6c9;
        font-size: 1.3rem;
        outline: 0;
        border-radius: 5px;
        padding: 3%;
    }

    .inputs > div > label {
        position: absolute;
        left: 3%;
        font-size: 1.2rem;
        color: #267a7a;
        pointer-events: none;
        transition: .5s;
        font-weight: bolder;
    }

    .inputs > div > input:focus ~ label, .inputs > div > input:valid ~ label {
        transform: translateY(-22px);
        color: #22272e;
    }

    button {
        width: 50%;
        height: 30px;
        border: none;
        border-radius: 5px;
        background: #ff8b3f;
        color: #22272e;
        font-size: 1.3rem;
        font-weight: bolder;
        cursor: pointer;
        transition: .5s;
    }

    button:hover {
        background: transparent;
        color: #ff8b3f;
        border: 3px solid #ff8b3f;
    }

    .dark {
        background: #ff8b3f !important;
    }

    .dark h2 {
        color: #f1f1f1 !important;
    }

    .dark .inputs > div > input {
        border-bottom: 1px solid #f1f1f1 !important;
        background: #f1f1f1 !important;
        color: #22272e !important;
    }

    .dark .inputs > div > label {
        color: #ff8b3f !important;
    }

    .dark .inputs > div > input:focus ~ label, .dark .inputs > div > input:valid ~ label {
        color: #f1f1f1 !important;
    }
    .dark button {
        background: #267a7a !important;
        color: #f1f1f1 !important;
    }

    .dark button:hover {
        background: transparent !important;
        color: #267a7a !important;
        border: 3px solid #267a7a !important;
    }
</style>