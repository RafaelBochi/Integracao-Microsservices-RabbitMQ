<script>
import { ref } from 'vue'

const username = ref('')
const password = ref('')
const email = ref('')

function createUser() {

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
}

button {
  background-color: rgb(18, 187, 18);
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