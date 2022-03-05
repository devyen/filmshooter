<template>
  <div class="modal fade" id="ProfileUpdateModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">프로필 작성</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <input type="text" class="form-control my-1" placeholder="프로필 메시지" aria-label="Profile Message" v-model="credentials.profile_message">
          <input type="text" class="form-control my-1" placeholder="선호하는 장르1" aria-label="선호하는 장르1" v-model="credentials.favorite_genre_1">
          <input type="text" class="form-control my-1" placeholder="선호하는 장르2" aria-label="선호하는 장르2" v-model="credentials.favorite_genre_2">
          <input type="text" class="form-control my-1" placeholder="선호하는 장르3" aria-label="선호하는 장르3" v-model="credentials.favorite_genre_3" @keyup.enter="signup">
          <div class="d-none" id="profile-error">
            실패!
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="putMyProfile" data-bs-dismiss="modal">수정</button>
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
  name: 'ProfileForm',
  props: {
    nickname: String,
    profile: Object,
    },
  data() {
    return {
      serverHost: 'http://127.0.0.1:8000',
      credentials : {
        profile_message: this.profile.profile_message,
        favorite_genre_1: this.profile.favorite_genre_1,
        favorite_genre_2: this.profile.favorite_genre_2,
        favorite_genre_3: this.profile.favorite_genre_3,
      }
    }
  },
  methods: {
    ...mapActions(['loginAction']),
    tokenHeader() {
      const token = localStorage.getItem('token')
      return {
        Authorization: `Token ${token}`
      }
    },
    fetchUserDetail() {
      axios({
        method: 'get',
        url: `${this.serverHost}/accounts/${this.nickname}/`
      })
        .then(res => {
          this.$emit('update-profile', res.data)
        })
        .catch(err => console.error(err))
    },
    putMyProfile() {
      axios({
        method: 'put',
        url: `${this.serverHost}/accounts/${this.nickname}/`,
        headers: this.tokenHeader(),
        data: this.credentials

      })
        .then(res => {
          console.log(res)
          this.fetchUserDetail()
        })
        .catch(err => console.error(err))
    }
  }
}
</script>

<style>

</style>