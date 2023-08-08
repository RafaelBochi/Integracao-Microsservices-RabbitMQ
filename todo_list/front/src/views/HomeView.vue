<script setup>
import { ref } from 'vue'
import producerApi from '../api/producer.js'

const producer = new producerApi()

const username = ref('')
const password = ref('')
const email = ref('')

async function createUser() {
  let user = {
    username: username.value,
    password: password.value,
    email: email.value
  }
  await producer.createUser(user)
}

</script>

<template>
  <div>
    <h1>Página Login - Teste RabbitMQ</h1>

    <div class="inputs">

      <input type="text" placeholder="Username" v-model="username">
      <input type="text" placeholder="Password" v-model="password">
      <input type="text" placeholder="Email" v-model="email">

      <button @click="createUser()">Confirm</button>

    </div>
  </div>
</template>


<style scoped>
h1 {
  text-align: center;
  margin: 20px;
  font-family: 'Courier New', Courier, monospace;
  font-weight: 100;
  color: #ff8b3f;
}

.inputs {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

input {
  margin: 10px;
  padding: 10px;
  width: 300px;
  border-radius: 5px;
  border: 1px solid #ccc;
  background-color: #f1f1f1;
}

button {
  background-color: #267a7a;
  color: white;
  font-size: small;
  border: 0;
  cursor: pointer;
  border-radius: 15px;
  width: 100px;
  height: 30px;
  font-weight: bold;
}

button:hover {
  transform: scale(1.05);
}

button:active{
  transform: scale(0.9);
}

</style>