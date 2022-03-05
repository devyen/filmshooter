<template>
  <div class="card my-4">
    <h2 class="mt-4 ms-4 mb-3">{{ nickname }}</h2>
    <h5 class="ms-4 message">{{ profile.profile_message }}</h5>
    <div class="row">

    </div>
    <div class="row">
      <span class="my-4 ms-4 col-9">좋아하는 장르: {{ profile.favorite_genre_1 }}, {{ profile.favorite_genre_2 }}, {{ profile.favorite_genre_3 }}</span>
      <span v-if="user.nickname==nickname" class="ms-4 pt-4 text-end col-2" data-bs-toggle="modal" data-bs-target="#ProfileUpdateModal">
        <i class="fas fa-edit"></i>
      </span>
    </div>
    <profile-update-form @update-profile="updateProfile" :profile="profile" :nickname="nickname"></profile-update-form>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import ProfileUpdateForm from '@/components/ProfileUpdateForm'
export default {
  name: 'ProfileUser',
  props:{
    profile: Object,
    nickname: String,
  },
  components: {
    ProfileUpdateForm,
  },
  methods: {
    updateProfile(newProfile) {
      this.$emit('update-profile', newProfile)
    }
  },
  computed: {
    ...mapState(['user'])
  }
}
</script>

<style>

.message {
  color: #999;
}

</style>