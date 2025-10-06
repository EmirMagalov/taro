<script setup>
import Header from './components/Header.vue'
import { ref,provide } from 'vue';


</script>

<template>
  <Header />

  <div class="xl:w-[90%] min-h-screen bg-gradient-to-r from-black to-[#ac8b49] pt-5 pb-20">
    <RouterView />
  </div>
</template>
