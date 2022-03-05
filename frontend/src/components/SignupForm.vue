<template>
  <div class="modal fade" id="signupModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered" style="width:20rem;">
      <div class="modal-content p-2">
        <div class="modal-header">
          <h5 class="modal-title">회원가입</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body pb-2">
          <input type="text" class="form-control my-2" placeholder="아이디" aria-label="Username" v-model="credentials.username">
          <input type="text" class="form-control my-2" placeholder="닉네임" aria-label="Nickname" v-model="credentials.nickname">
          <input type="password" class="form-control my-2" placeholder="비밀번호" aria-label="Password" v-model="credentials.password1">
          <input type="password" class="form-control my-1" placeholder="비밀번호 확인" aria-label="Password Confirm" v-model="credentials.password2" @keyup.enter="signup">
        </div>
        <div class="container-fluid text-end">
          <span class="d-none badge bg-warning mb-2" id="signup-error">
            회원가입 실패!
          </span>
          <button type="button" class="btn btn-primary text-white mt-1 mb-2 col-12" @click="signup">회원가입</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
// import { Modal } from 'bootstrap'

export default {
  name: 'SignupForm',
  data() {
    return {
      serverHost: 'http://127.0.0.1:8000',
      credentials : {
        username: '',
        nickname: '',
        password1: '',
        password2: '',
      }
    }
  },
  methods: {
    ...mapActions(['loginAction']),
    signup() {
      axios({
        method: 'post',
        url: `${this.serverHost}/dj_rest_auth/registration/`,
        data: this.credentials
      })
        .then(res => {
          localStorage.setItem('token', res.data.key)
          localStorage.setItem('user', JSON.stringify(res.data.user))
          this.loginAction(res.data.user)

          const body = document.querySelector('body')
          body.classList.remove('modal-open')
          body.style.removeProperty('overflow')
          body.style.removeProperty('padding-right')

          // 모달창 안 꺼지는 문제 해결
          const myModal = document.querySelector('#signupModal')
          myModal.classList.remove("in")
          document.querySelector(".modal-backdrop").remove()
          myModal.style.display = "none"
          this.credentials = {
            username: '',
            nickname: '',
            password1: '',
            password2: '',
         }
        })
        .catch(err => {
          console.error(err)
          const errorMessage = document.querySelector('#signup-error')
          errorMessage.classList.remove('d-none')
        })
    }
  }
}
</script>

<style>

</style>