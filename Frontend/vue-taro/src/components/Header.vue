<script setup>
import { ref, watch, inject } from 'vue'
import { useRoute } from 'vue-router'

const isOpenFortune = inject('isOpenFortune')
const isOpenMenu = ref(false)

const route = useRoute()

watch(
  () => route.fullPath,
  () => {
    console.log('Маршрут изменился!')
    // например:
    isOpenMenu.value = false
  },
)

const menu = {
  'На главную': { path: '/', icon: '/home-svgrepo-com.svg' },
  'Комната гадания': { path: '/freetaro', icon: '' },
  'Шар судьбы(скоро)': { path: '', icon: '' },
  'Сонник(скоро)': { path: '', icon: '' },
}
</script>

<template>
  <div
    v-show="isOpenMenu"
    @click="isOpenMenu = false"
    class="fixed h-screen bg-black/80 w-full z-10"
  >
    <div @click.stop class="fixed h-screen bg-[#f8ca7f] w-50 z-2">
      <div class="flex flex-col gap-3 font-bold">
        <a class="text-[#2b7fff] underline hover:text-[#2b7fff]" href="https://t.me/iamgukk">
          <div class="flex pt-5 text-xs">
            <img src="/telegram-svgrepo-com.svg" width="15" alt="" />
            <p class="font-bold">Запись на индивидуальное гадание</p>
          </div>
        </a>
        <div v-for="(item, name) in menu" :key="name">
          <router-link
            :to="item.path"
            class="flex items-center p-2"
            :activeClass="[item.path ? 'bg-[#e1e6db]' : '']"
          >
            <p class="text-sm">{{ name }}</p>
          </router-link>
        </div>
      </div>
    </div>
  </div>

  <div class="bg-gradient-to-t from-white to-[#CCFFFF] p-2">
    <div class="relative flex flex-col items-center justify-center">
      <!-- центр -->
      <div class="text-5xl xl:text-8xl custom-font flex gap-1 items-center justify-center">
        <img src="/logo.png" alt="" class="w-10 lg:w-15 xl:w-20" />
        <router-link to="/"><h1>TaroGuk.com</h1></router-link>
      </div>

      <!-- правый блок -->
      <div class="hidden xl:block xl:absolute xl:right-6 gap-2 flex flex-col text-sm xl:text-lg">
        <!-- <div class="flex items-center justify-center gap-1">
        <img src="/whatsapp-svgrepo-com.svg" class="w-4 xl:w-5" alt="" />
        <p class="">+994553749099</p>
      </div> -->
        <a class="text-[#2b7fff] underline hover:text-[#2b7fff]" href="https://t.me/iamgukk">
          <div class="flex gap-1 items-center justify-center">
            <p class="font-bold">Запись на индивидуальное гадание</p>
            <img src="/telegram-svgrepo-com.svg" width="20" alt="" />
            <!-- <a class="hover:opacity-80" href="https://www.instagram.com/iamgukk/"
          ><img src="/instagram-svgrepo-com.svg" width="20" alt=""
        /></a> -->
          </div>
        </a>
      </div>
    </div>
    <div class="text-center">
      <div
        @click="((isOpenMenu = true), (isOpenFortune = false))"
        class="inline-block mt-2 xl:hidden"
      >
        <img src="/menu-svgrepo-com.svg" class="w-7" alt="" />
      </div>
    </div>
    <div class="hidden xl:block mt-5 gap-2 text-sm xl:text-lg font-bold">
      <div class="flex items-center justify-center gap-5">
        <div
          v-for="(item, name) in menu"
          :key="name"
          class="flex items-center gap-0 hover:text-yellow-300"
        >
          <router-link :to="item.path">
            <div class="flex gap-1">
              <img v-show="item.icon" class="w-5" :src="item.icon" alt="" />
              <p>{{ name }}</p>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@font-face {
  font-family: 'MyCustomFont';
  src: url('@/assets/Fonts/paperland.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

.custom-font {
  font-family: 'MyCustomFont', sans-serif;
}
</style>
