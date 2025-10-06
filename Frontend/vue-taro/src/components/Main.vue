<script setup>
import CardBack from './CardBack.vue'
import Candle from './Candle.vue'
import { onMounted, ref, nextTick, inject } from 'vue'
import axios from 'axios'
import { url } from '@/config'
const reset = ref(false)
const allCards = ref([]) // сюда сохраним все карточки
const taroItems = ref([]) // текущие 5 карточек
const taroText = ref([])
const isOpenFortune = ref(false)
const getData = async () => {
  // Загружаем данные только один раз
  if (allCards.value.length === 0) {
    const { data } = await axios.get(url)
    allCards.value = data
  }

  // Перемешиваем и выбираем 5 случайных
  taroItems.value = allCards.value.sort(() => 0.5 - Math.random()).slice(0, 5)
}
onMounted(() => {
  getData()
})

const selected = ref('')
const fortune_telling_dict = {
  'Гадание на любовь и отношения': 'love_text',
  'Гадание на бизнес и карьеру': 'work_text',
  'Карта дня': 'day_text',
  'Совет карты': 'advice_text',
  'Ответ на вопрос Да и Нет': 'yesno_text',
}

const fortune_telling_options = ref('love_text') // какое поле брать
const fortune_telling_options_text = ref('Гадание на любовь и отношения') // заголовок
const cardQuant = ref(5)
const order_of_opening_text = ref('Открывайте каждую карту')

const ChooseFortuneTelling = (fortuneKey, fortuneValue) => {
  getData()
  fortune_telling_options.value = fortuneValue
  fortune_telling_options_text.value = fortuneKey
  isOpenFortune.value = false
  selected.value = fortuneKey
  if (fortuneValue === 'work_text') {
    cardQuant.value = 3
    order_of_opening_text.value = 'Открывайте каждую карту'
  } else if (fortuneValue === 'day_text') {
    cardQuant.value = 1
    order_of_opening_text.value = 'Открывайте карту'
  } else if (fortuneValue === 'advice_text') {
    cardQuant.value = 1
    order_of_opening_text.value = 'Открывайте карту'
  } else if (fortuneValue === 'yesno_text') {
    cardQuant.value = 1
    order_of_opening_text.value = 'Открывайте карту'
  } else {
    cardQuant.value = 5
    order_of_opening_text.value = 'Открывайте каждую карту'
  }
  reset.value = true
}
nextTick(() => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
})

const cardBack = Array(7)
  .fill()
  .map(() => '/taro on the back.png')
</script>

<template>
  <div class="flex justify-center mb-5 2xl:hidden relative h-15">
    <div
      v-if="isOpenFortune"
      class="bg-black/50 fixed min-h-screen inset-0 z-10"
      @click="isOpenFortune = false"
    ></div>

    <div class="w-60 md:w-80 md:text-lg relative">
      <!-- Кнопка -->
      <button
        @click="isOpenFortune = !isOpenFortune"
        class="w-full bg-black/20 text-white font-bold p-2 rounded shadow cursor-pointer flex justify-center items-center space-x-2"
      >
        <candle />
        <span class="flex-1 text-center"
          >{{ selected || Object.keys(fortune_telling_dict)[0] }}
          {{ isOpenFortune ? '▲' : '▼' }}</span
        >
        <candle />
      </button>

      <!-- Выпадающий список -->
      <ul
        v-if="isOpenFortune"
        class="absolute left-0 w-full font-bold text-shadow-xs text-shadow-black bg-black/80 bg-gradient-to-t from-black/80 to-yellow-100/80 text-white mt-1 rounded shadow-lg max-h-60 overflow-y-auto z-10"
      >
        <li
          v-for="(value, key) in fortune_telling_dict"
          :key="key"
          @click="ChooseFortuneTelling(key, value)"
          class="p-2 hover:bg-yellow-500 hover:text-black cursor-pointer"
        >
          {{ key }}
        </li>
      </ul>
    </div>
  </div>

  <div class="flex flex-wrap gap-15 justify-center">
    <div>
      <div class="flex relative items-center justify-center">
        <img class="object-cover" src="/table.png" alt="" />
        <CardBack
          v-model:cards="cardBack"
          :cardQuant="cardQuant"
          :taroItems="taroItems"
          v-model:taroText="taroText"
          v-model:reset="reset"
        />
      </div>
      <div
        class="text-white font-bold text-sm md:text-md lg:text-lg xl:text-xl text-center 2xl:hidden"
      >
        {{ order_of_opening_text }}
      </div>
    </div>
    <div class="hidden 2xl:block">
      <div class="flex gap-20 justify-center">
        <candle />
        <candle />
        <candle />
        <!-- <candle />
          <candle />
          <candle />
          <candle />
          <candle />
          <candle /> -->
      </div>
      <div
        class="text-xl bg-gradient-to-t from-black/80 to-yellow-100/80 max-h-120 p-5 rounded-xl inset-shadow-2xs shadow-black"
      >
        <p class="mb-5 text-2xl font-bold text-black text-center w-80 mx-auto break-words">
          {{ fortune_telling_options_text }}
        </p>
        <h1
          v-for="(fortuneValue, fortuneKey) in fortune_telling_dict"
          :key="fortuneKey"
          @click="ChooseFortuneTelling(fortuneKey, fortuneValue)"
          class="bg-black/20 font-bold shadow-lg rounded-t-lg border-b border-black text-shadow-lg text-white cursor-pointer hover:text-[#f4c901] hover:opacity-80 m-2 p-2"
        >
          {{ fortuneKey }}
        </h1>
        <h1 class="mt-5 text-xl text-shadow-sm shadpw-black font-bold text-center text-white">
          {{ order_of_opening_text }}
        </h1>
      </div>
    </div>
  </div>
  <div class="mt-5">
    <div v-if="taroText.length != 0">
      <div v-for="ti in taroText" :key="ti">
        <div
          class="text-sm md:text-base lg:text-lg xl:text-xl shadow-xs bg-black/40 mx-auto shadow-white text-white p-3 w-[80%]"
        >
          <h1 class="font-bold text-[#f4c901]">{{ ti.name }}</h1>
          <p class="text-shadow-xs text-shadow-black">{{ ti[fortune_telling_options] }}</p>
        </div>
      </div>
    </div>
    <div v-else>
      <div
        class="font-bold border-l-6 border-[#f8ca7f] text-sm md:text-base lg:text-lg xl:text-xl text-center shadow-xs bg-black/40 mx-auto shadow-white text-white p-5 h-25 w-[80%]"
      >
        <h1>
          Пользуйтесь данным раскладом не слишком часто, так как это может ввести вас в заблуждение.
        </h1>
      </div>
    </div>
  </div>
</template>
