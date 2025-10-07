<script setup>
import { computed, reactive, ref, watch } from 'vue'

const props = defineProps({
  cardQuant: Number,
  cards: Array, // исходные изображения (карты сзади)
  taroItems: Array, // "лицевые" карты, которые будем открывать
  taroText: Array,
  reset: Boolean,
})
const flipped = reactive(Array(props.cards.length).fill(false))
const emit = defineEmits(['update:cards', 'update:taroText', 'update:reset'])

// создаём реактивный массив текущих карт на столе
const currentCards = reactive([...props.cards])

// Генерируем сетку с объектами {img, index}, чтобы индекс совпадал с currentCards

const resetCards = () => {
  for (let i = 0; i < flipped.length; i++) {
    flipped[i] = false
    currentCards[i] = props.cards[i] // вернуть рубашку
  }
  emit('update:taroText', []) // очистить данные
}

watch(
  () => props.reset,
  (newVal) => {
    if (newVal) {
      resetCards()
      emit('update:reset', false)
    }
  },
)

const grid = computed(() => {
  const rows = []
  let counter = 0

  switch (props.cardQuant) {
    case 1:
      rows.push([null])
      rows.push([{ img: currentCards[counter], index: counter++ }])
      rows.push([null])
      break
    case 3:
      rows.push([null])
      rows.push([
        { img: currentCards[counter], index: counter++ },
        { img: currentCards[counter], index: counter++ },
        { img: currentCards[counter], index: counter++ },
      ])
      rows.push([null])
      break
    case 5:
      rows.push([null, { img: currentCards[counter], index: counter++ }, null])
      rows.push([
        { img: currentCards[counter], index: counter++ },
        { img: currentCards[counter], index: counter++ },
        { img: currentCards[counter], index: counter++ },
      ])
      rows.push([null, { img: currentCards[counter], index: counter++ }, null])
      break
    case 7:
      rows.push([null, { img: currentCards[counter], index: counter++ }, null])
      rows.push([
        { img: currentCards[counter], index: counter++ },
        { img: currentCards[counter], index: counter++ },
        { img: currentCards[counter], index: counter++ },
      ])
      rows.push([
        { img: currentCards[counter], index: counter++ },
        { img: currentCards[counter], index: counter++ },
        { img: currentCards[counter], index: counter++ },
      ])
      break
    default:
      return []
  }

  return rows
})

// Функция клика по карте
const flipCard = (index) => {
  const cardObj = props.taroItems[index]
  if (!flipped[index]) {
    // показать лицевую

    if (cardObj) {
      currentCards[index] = currentCards[index] = 'https://flexado.xyz/media/photo/card_a6db59.jpg'
      flipped[index] = true

      // добавить только если такого объекта еще нет
      const alreadyAdded = props.taroText.some((item) => item.id === cardObj.id)
      if (!alreadyAdded) {
        emit('update:taroText', [...props.taroText, cardObj])
      }
    }
  } else {
    // вернуть рубашку
    currentCards[index] = props.cards[index]
    flipped[index] = false
    const newData = props.taroText.filter((item) => item.id !== cardObj.id)
    emit('update:taroText', newData)
  }
}
</script>

<template>
  <div class="absolute flex flex-col">
    <div v-for="(row, rowIndex) in grid" :key="rowIndex" class="flex justify-center gap-4">
      <div
        class="flex flex-col w-15 md:w-30 lg:w-35 xl:w-40"
        v-for="(card, colIndex) in row"
        :key="colIndex"
      >
        <img
          v-if="card"
          :src="card.img"
          class="w-15 md:w-30 lg:w-35 xl:w-40 object-cover cursor-pointer"
          @click="flipCard(card.index)"
        />
        <div>
          <h1
            :class="[
              card && flipped[card.index] ? 'bg-black/80 md:bg-transparent' : '',
              'font-bold  text-[#f4c901] lg:h-15 text-center break-words  text-[6px] md:text-xs lg:text-lg text-shadow-lg text-shadow-black',
            ]"
          >
            {{ card && flipped[card.index] ? taroItems[card?.index]?.name : '\u00A0' }}
          </h1>
        </div>
      </div>
    </div>
  </div>
</template>
