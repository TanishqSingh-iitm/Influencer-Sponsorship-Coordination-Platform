<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h2>It is a part of the Vue.js frontend</h2>
    <h3>goodbye</h3>
  </div>
  <div class="card flex justify-center">
        <DatePicker v-model="date" />
  </div>
  <img width="100" height="100" src="https://img.icons8.com/nolan/100/crowdfunding.png" alt="crowdfunding"/>
</template>
<script setup>
  import { ref } from "vue";
  
  const date = ref();


</script>
<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
