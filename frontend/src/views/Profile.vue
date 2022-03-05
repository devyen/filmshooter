<template>
  <div class="mt-5">
    <div class="offset-2 col-8 mt-4">
      <div v-if="!profile&user.nickname==nickname" class="d-flex flex-column align-items-center">
        <h4 class="m-4">나만의 취향을 담은 프로필을 만들어보세요!</h4>
        <button type="button" class="btn btn-primary text-light" data-bs-toggle="modal" data-bs-target="#ProfileModal">
          프로필만들기
        </button>
        <profile-form :nickname="nickname" @profile-created="fetchUserDetail"></profile-form>
      </div>
      <div v-else>
        <div class="fs-2 text-center">
          <span class="fw-bold text-primary">{{nickname}}</span>
          <span> 님의 프로필페이지입니다</span>
        </div>
        <profile-user @update-profile="updateProfile" :profile="profile" :nickname="nickname"></profile-user>
        <profile-statistic :profile="profile" :nickname="nickname"></profile-statistic>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import ProfileUser from '@/components/ProfileUser'
import ProfileStatistic from '@/components/ProfileStatistic'
import ProfileForm from '@/components/ProfileForm'

export default {
  name: 'Profile',
  components: {
    ProfileUser,
    ProfileStatistic,
    ProfileForm,
  },
  data() {
    return {
      serverHost: 'http://127.0.0.1:8000',
      nickname: this.$route.params.nickname,
      profile: null,
    }
  },
  methods: {
    fetchUserDetail() {
      axios({
        method: 'get',
        url: `${this.serverHost}/accounts/${this.nickname}/`
      })
        .then(res => {
          this.profile = res.data
        })
        .catch(err => console.error(err))
    },
    updateProfile(newProfile) {
      this.profile = newProfile
    }
  },
  computed: {
    ...mapState(['user'])
  },
  created() {
    this.fetchUserDetail()
  }
}
</script>

<style>

</style>