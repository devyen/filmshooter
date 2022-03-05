<template>
  <div class="modal fade" id="loginModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered" style="width:20rem;">
      <div class="modal-content p-2">
        <div class="modal-header">
          <h5 class="modal-title">로그인</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body pb-1">
          <input type="text" class="form-control my-3" placeholder="아이디" aria-label="Username" v-model="credentials.username">
          <input type="password" class="form-control" placeholder="비밀번호" aria-label="Password" v-model="credentials.password" @keyup.enter="login">
        </div>
        <div class="container-fluid text-end">
          <span class="d-none badge bg-warning mt-2 mb-2" id="login-error">
            로그인 실패!
          </span>
          <button type="button" class="btn btn-primary text-white col-12 mt-2 mb-3" @click="login">로그인</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import axios from 'axios'
// import { Modal } from 'bootstrap'

export default {
  name: 'LoginForm',
  data() {
    return {
      serverHost: 'http://127.0.0.1:8000',
      credentials : {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    ...mapActions(['loginAction']),
    login() {
      axios({
        method: 'post',
        url: `${this.serverHost}/dj_rest_auth/login/`,
        data: this.credentials,
      })
        .then(res => {
          localStorage.setItem('token', res.data.key)
          localStorage.setItem('user', JSON.stringify(res.data.user))
          this.loginAction(res.data.user)
          // 모달 창 수동으로 끄기
          // const loginModal = new Modal(document.getElementById('loginModal'))
          // loginModal.hide()
          const body = document.querySelector('body')
          body.classList.remove('modal-open')
          body.style.removeProperty('overflow')
          body.style.removeProperty('padding-right')
          // 모달창 안 꺼지는 문제 해결
          const myModal = document.querySelector('#loginModal')
          myModal.classList.remove("in")
          document.querySelector(".modal-backdrop").remove()
          myModal.style.display = "none"
          this.credentials = {
            username: '',
            password: '',
          }
        })
        .catch(err => {
          console.error(err)
          const errorMessage = document.querySelector('#login-error')
          errorMessage.classList.remove('d-none')
        })
    },
  }
}
</script>

<style>

</style>