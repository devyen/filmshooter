import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Detail from '../views/Detail.vue'
import Review from '../views/Review.vue'
import Profile from '../views/Profile.vue'
import Recommend from '../views/Recommend.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/detail/:movieId',
    name: 'Detail',
    component: Detail
  },
  {
    path: '/review/:reviewId',
    name: 'Review',
    component: Review
  },
  {
    path: '/profile/:nickname',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
