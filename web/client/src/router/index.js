import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        title: 'MedSoc Shuffle'
      }
    }
  ]
})

router.beforeEach((to) => {
  const title = to.meta.title
  const defaultTitle = 'Default Title'

  document.title = title || defaultTitle
})

export default router
