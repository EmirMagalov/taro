<template>
  <div class="inline-flex flex-col items-center mt-0">
    <!-- Пламя свечи -->
    <div
      class="w-3 h-4 2xl:w-5 2xl:h-7 bg-gradient-to-b from-yellow-200 via-orange-400 to-transparent rounded-full animate-flicker mb-[-10px]"
    ></div>

    <!-- Тело свечи -->
    <div
      class="w-4 h-10 2xl:w-10 2xl:h-24 bg-gradient-to-b from-white to-yellow-100 rounded-md shadow-md"
    ></div>
  </div>
</template>

<style>
@keyframes flicker {
  0% {
    transform: scale(1) translateY(0);
    opacity: 1;
  }
  50% {
    transform: scale(1.1, 0.9) translateY(-2px);
    opacity: 0.8;
  }
  100% {
    transform: scale(0.9, 1.1) translateY(2px);
    opacity: 1;
  }
}

.animate-flicker {
  animation: flicker 0.4s infinite alternate;
}
</style>
