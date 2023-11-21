<script setup>
import { ref } from 'vue'
import axios from 'axios'

const isIn = ref(true)
const email = ref('')
const password = ref('')

function sendData() {
  axios({
    method: 'post',
    url: 'https://jsonplaceholder.typicode.com/posts',
    data: {
      email: email,
      password: password
    }
  })
    .then(function (response) {
      console.log(response.status)
    })
    .catch(function (error) {
      console.log(error)
    })
}
</script>
<template>
  <div class="form" style="padding: 10px">
    <div class="sing-in">
      <h1 style="text-align: center; color: #41b883">{{ isIn ? 'Sing in' : 'Sing up' }}</h1>

      <div style="height: 100%; text-align: center">
        <input v-model="email" class="in" placeholder="email" />
        <input v-model="password" class="in" placeholder="password" />
        <button @click="sendData" class="in but cursor">
          {{ isIn ? 'Login' : 'Regestration' }}
        </button>
        <br /><br />

        <a @click="isIn = !isIn" class="in cursor" style="position: relative; bottom: 1px">
          {{ isIn ? 'Sing up' : 'Sing in' }}
        </a>
      </div>
    </div>

    <!-- <div v-else class="sing-up">
      <h1 style="text-align: center">Sing up</h1>

      <div style="height: 100%; text-align: center; ">
      <input class="in" placeholder="email" />
      <input class="in" placeholder="password" />
      <input class="in" placeholder="password" />

      <button class="in but cursor ">Login</button>
      <br>

      <a @click="isIn = !isIn" class="in cursor" style="position: relative; bottom: 1px;">Sing in</a>
    </div>   -->

    <!-- </div> -->
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .login {
    min-height: 100vh;
    display: flex;
    align-items: end;
  }
}

.form {
  height: 100%;
  width: 60%;
  border: 0.2rem solid;
  border-radius: 30px;
}

.in {
  display: inline;
  align-self: end;
  width: 80%;
  border-radius: 10px;
  padding: 5px 10px;
  margin: 5px 1px;
}

.but {
  width: 50%;
  color: #34495e;
  background-color: #41b883;
  border: solid #34495e;
}

.cursor {
  cursor: pointer;
}

.sing-in {
}

.sing-up {
}
</style>
