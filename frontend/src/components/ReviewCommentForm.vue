<template>
  <div class="my-3">
    <input v-if="isLoggedIn" v-model="myComment" placeholder="코멘트 남기기" type="text" @keyup.enter="postMyComment" class="form-control">
    <p v-else>코멘트를 남기려면 로그인이 필요합니다.</p>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'ReviewCommentForm',
  data() {
    return {
      myComment: '',
      reviewId: this.$route.params.reviewId,
    }
  },
  methods: {
    ...mapActions(['fetchReview']),
    tokenHeader() {
      const token = localStorage.getItem('token')
      return {
        Authorization: `Token ${token}`
      }
    },
    postMyComment() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/reviews/${this.reviewId}/comments/`,
        headers: this.tokenHeader(),
        data: {
          content: this.myComment,
          review: this.reviewId
        }
      })
        .then(() => {
          this.fetchReview(this.reviewId)
          this.myComment = ''
        })
        .catch(err => console.error(err))
    },
  },
  computed: {
    ...mapState(['isLoggedIn']),

  }
}
</script>

<style>

</style>