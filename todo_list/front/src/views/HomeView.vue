<script setup>
import { ref, provide } from 'vue'
import consumerApi from '../api/consumer.js'

import Tasks from '@/components/Tasks.vue'
import Add_Tasks from '@/components/Add_Tasks.vue'

const showModal = ref(false)

function openModal() {
  showModal.value = true
}

function closeModal() {
  showModal.value = false
}

provide('closeModal', closeModal)

</script>

<template>
  <main>
    <div :class="{'blurred': showModal, 'cover': true}">
      <img src="/logo_dark.png" alt="Fábrica de Software" class="logo">
      <button @click="openModal">
        Tarefas
      </button>
      <Tasks />
    </div>
    <Add_Tasks v-if="showModal" class="add"/>
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
  height: 100%;
  background-color: #22272e;
}

button{
  position: absolute;
  top: 10%;
  left: 1%;
  border: none;
  padding: 5px;
}

.add {
  position: absolute;
  top: 25%;
  left: 30%;
}

.blurred {
  filter: blur(5px);
}

.cover {
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