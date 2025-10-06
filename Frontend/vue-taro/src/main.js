import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './assets/main.css'
import App from './App.vue'
import Main from './components/Main.vue'
import FreeTaro from './components/FreeTaro.vue'

const routes = [
  { path: '/', name: 'Main', component: Main },
  { path: '/freetaro', name: 'FreeTaro', component: FreeTaro },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

const app = createApp(App)
app.use(router)
app.mount('#app')
