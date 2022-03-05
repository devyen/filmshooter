<template>
  <div class="modal fade" id="reviewCreateModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">당신의 평가를 남겨주세요!</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <textarea rows="5" v-model="myReview" type="text" class="form-control py-3"></textarea>
          <star-form @rate-selected="rateSelected"></star-form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="postMyReview" data-bs-dismiss="modal">작성</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapState } from 'vuex'
import StarForm from '@/components/StarForm'

export default {
  name: 'MovieDetailReviewForm',
  data() {
    return {
      myReview: '',
      myRate: 0
    }
  },
  components: {
    StarForm
  },
  methods: {
    ...mapActions(['fetchReviewList']),
    tokenHeader() {
      const token = localStorage.getItem('token')
      return {
        Authorization: `Token ${token}`
      }
    },
    rateSelected(rate) {
      this.myRate = rate
    },
    postMyReview() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/reviews/movie/${this.movieDetail.id}/`,
        headers: this.tokenHeader(),
        data: {
          content: this.myReview,
          rate: this.myRate,
          movie: this.movieDetail.id,
        }
      })
        .then(() => {
          this.fetchReviewList(this.movieDetail.id)
          this.myReview = ''
          this.myRate = 0
        })
        .catch(err => console.error(err))
    }
  },
  computed: {
    ...mapState(['movieDetail']),
  }
}
</script>

<style>

</style>