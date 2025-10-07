<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { url } from '@/config'

const fortune_telling_dict = {
  'Значение в любовных отношениях': 'love_text',
  'Значение в бизнесе и работе': 'work_text',
  'Значение карты дня': 'day_text',
  'Совет карты': 'advice_text',
  'Ответ на вопрос Да и Нет': 'yesno_text',
}

const allCards = ref([]) // Все карты
const taroItems = ref([]) // Колода на столе
const selectCardsList = ref([]) // Выбранные карты
const selectCardsText = ref('')
const getData = async () => {
  if (allCards.value.length === 0) {
    const { data } = await axios.get(url)
    allCards.value = data
  }
  taroItems.value = [...allCards.value] // копируем все карты
  selectCardsList.value = []
}

onMounted(getData)

// Выбор случайной карты
const selectCard = () => {
  if (selectCardsList.value.length >= 16) return

  if (taroItems.value.length === 0) {
    console.log('Все карты уже на столе')
    return
  }

  const randomIndex = Math.floor(Math.random() * taroItems.value.length)
  const card = taroItems.value.splice(randomIndex, 1)[0] // удаляем из колоды
  selectCardsList.value.push(card) // добавляем на стол
}

// Возврат всех карт
const returnCards = () => {
  taroItems.value = [...allCards.value]
  selectCardsList.value = []
  selectCardsText.value = ''
}
</script>

<template>
  <div class="flex items-center justify-center">
    <div class="relative">
      <img class="object-cover" src="/table.png" alt="" />

      <!-- Колода -->
      <div @click="selectCard" class="absolute top-1/2 -translate-y-1/2 cursor-pointer">
        <img src="/taro on the back.png" class="mx-auto w-12 lg:w-15 xl:w-30" alt="" />
        <p class="text-white text-[10px] font-bold text-center xl:text-xl">
          {{ taroItems.length }}
        </p>
      </div>

      <!-- Выбранные карты -->
      <div
        class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 grid grid-cols-4 gap-1"
      >
        <div
          @click="selectCardsText = card"
          v-for="card in selectCardsList"
          :key="card.id"
          class="flex flex-col items-center cursor-pointer"
        >
          <img :src="card.img.replace(/^http:/, 'https:')" class="w-15 lg:w-15 xl:w-30" alt="" />
          <p class="text-center font-bold text-[6px] xl:text-base text-[#f4c901]">
            {{ card.name }}
          </p>
        </div>
      </div>

      <!-- Кнопки -->
      <div class="absolute right-1 top-[40%] flex flex-col gap-5">
        <p
          class="bg-black/60 rounded-lg hover:bg-[#e1e6db] hover:text-black text-[12px] text-white font-bold xl:text-lg cursor-pointer"
          :class="{ invisible: selectCardsList.length === 0 }"
          @click="((selectCardsList = []), (selectCardsText = ''))"
        >
          Очистить стол
        </p>
        <p
          class="bg-black/60 rounded-lg hover:bg-[#e1e6db] hover:text-black text-[12px] text-white font-bold xl:text-lg cursor-pointer"
          :class="{ invisible: taroItems.length === allCards.length }"
          @click="returnCards"
        >
          Вернуть карты
        </p>
      </div>
    </div>
  </div>
  <div
    class="mt-3 text-sm md:text-base lg:text-lg xl:text-xl shadow-xs bg-black/40 mx-auto shadow-white text-white p-3 w-[80%]"
    v-if="selectCardsText"
  >
    <p class="text-center text-lg font-bold text-[#f4c901]">{{ selectCardsText.name }}</p>
    <h1 class="font-bold text-base text-[#ecc21a] underline xl:text-lg">Описание</h1>
    <p>{{ selectCardsText.descr_text }}</p>
    <div v-for="(value, key) in fortune_telling_dict" :key="key">
      <h1 class="font-bold text-base text-[#ecc21a] underline xl:text-lg">{{ key }}</h1>
      <p>{{ selectCardsText[value] }}</p>
    </div>
  </div>
</template>
