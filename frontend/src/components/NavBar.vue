<template>
<div>
  <login-form></login-form>
  <signup-form></signup-form>
  <login-signup-modal></login-signup-modal>
  <nav class="navbar navbar-expand navbar-dark fixed-top py-0">
    <router-link class="navbar-brand ps-2" to="/">
      <img src="@/assets/film_shooter_logo.png" alt="film_shooter_logo" style="width: 4.5em" class="p-1">
    </router-link>
    <div class="container-fluid container justify-content-end">
      <ul class="navbar-nav">
        <div v-if="!isLoggedIn">
          <a class="mx-2 pointer text-white" data-bs-toggle="modal" data-bs-target="#loginModal">로그인</a>
          <a class="mx-2 pointer text-white" data-bs-toggle="modal" data-bs-target="#signupModal">회원가입</a>
        </div>
        <div v-else>
          <span class="mx-2">
            <router-link class="text-white" :to="{ name: 'Profile', params: { nickname: user.nickname } }">프로필</router-link>
          </span>
          <span class="mx-2">
            <router-link class="text-white" :to="{ name: 'Recommend' }">내 취향 영화 추천</router-link>
          </span>
          <a class="mx-2 pointer text-white" @click="logout">로그아웃</a>
        </div>
      </ul>
    </div>
  </nav>
</div>
</template>

<script>
import LoginForm from '@/components/LoginForm'
import SignupForm from '@/components/SignupForm'
import LoginSignupModal from '@/components/LoginSignupModal'
import { mapState, mapActions } from 'vuex'
import axios from 'axios'

export default {
  name: 'NavBar',
  components: {
    LoginForm,
    SignupForm,
    LoginSignupModal,
  },
  data() {
    return {
      serverHost: 'http://127.0.0.1:8000'
    }
  },
  methods: {
    ...mapActions(['logoutAction']),
    logout() {
      axios({
        method: 'post',
        url: `${this.serverHost}/dj_rest_auth/logout/`,
      })
        .then(() => {
          localStorage.removeItem('token')
          localStorage.removeItem('user')
          this.logoutAction()
          if (this.$route.name !== 'Home'){
            this.$router.push({ name: 'Home' })
          }
        })
        .catch(err => console.error(err))
    }
  },
  computed: {
    ...mapState(['isLoggedIn', 'user']),
  },
  mounted() {
    const nav = this.$el.querySelector('nav')
    window.addEventListener('scroll', () => {
      if (window.scrollY !== 0) {
        nav.classList.add('bg-darker')
      } else {
        nav.classList.remove('bg-darker')
      }
    })
  },
}
</script>

<style>
.navbar {
  z-index: 10;
  transition: all 0.25s linear !important;
}
.pointer {
  cursor: pointer;
}
.bg-darker {
  background-color: #24262b;
}
</style>