<template>
  <div id="app">
    <nav-bar></nav-bar>
    <span class="back-button" @click="goBack">
      <div class="mb-2">back</div>
      <i class="far fa-arrow-alt-circle-left fs-2"></i>
    </span>
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'

import { mapActions } from 'vuex'
// import axios from 'axios'

export default {
  name: 'App',
  components: {
    NavBar,
  },
  data() {
    return {
      isLoggedIn: false,
      serverHost: 'http://127.0.0.1:8000',
    }
  },
  methods: {
    ...mapActions(['loginAction']),
    init() {
      const token = localStorage.getItem('token')
      if (token) {
        const user = JSON.parse(localStorage.getItem('user'))
        this.loginAction(user)
      }
    },
    goBack() {
      this.$router.go(-1)
    }
  },
  created() {
    this.init()
  }
}
</script>

<style lang="scss">
$primary: #a982f7;
$dark: #2c2c2c;
@import 'bootstrap/scss/bootstrap';
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Gothic+A1:wght@100;200;300;400;500;600;700;800;900&family=Gowun+Dodum&display=swap');

// 'Gowun Dodum', 'Gothic A1'
* {
  font-family: 'Noto Sans KR', sans-serif;
  color: white;
}

img {
  object-fit: scale-down;
}

a {
  text-decoration: none;
}

.back-button {
  position: fixed;
  z-index: 1050;
  top: 13%;
  left: 3%;
}

.back-button:hover > i{
  color: #999;
  transform: scale(1.2);
}

.modal-title {
  color: #121212;
}

.modal-body {
  color: #121212;
}

.card {
  background-color: #36383a;
  border: none;
}

.bg-custom-black {
  background: #141517
}

.bg-shore {
  background: #70e1f5;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #ffd194, #70e1f5);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #ffd194, #70e1f5); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

.bg-amin {
  background: #8E2DE2;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #4A00E0, #8E2DE2);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #4A00E0, #8E2DE2); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

.bg-dull {
  background: #C9D6FF;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #E2E2E2, #C9D6FF);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #E2E2E2, #C9D6FF); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

.bg-moonlit {
  background: #0F2027;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #2C5364, #203A43, #0F2027);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #2C5364, #203A43, #0F2027); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

.bg-deep {
  background: #000000;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to top, #434343, #000000);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to top, #434343, #000000); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

.bg-purplewhite {
  background: #BA5370;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to bottom, #F4E2D8, #BA5370);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to bottom, #F4E2D8, #BA5370); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

.bg-purplepink {
  background: #946cb6;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #a982f7, #fd80bb);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #8b53fa, #f8bfec); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

.bg-purple {
  background: #4568DC;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #B06AB3, #4568DC);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #B06AB3, #4568DC); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
</style>
