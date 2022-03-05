<template>
  <div class="modal fade" :id="modalId" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">당신의 평가를 남겨주세요!</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <textarea rows="5" v-model="myReview" type="text" class="form-control"></textarea>
          <update-star-form @rate-selected="rateSelected"></update-star-form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="putMyReview" data-bs-dismiss="modal">수정</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapState } from 'vuex'
import UpdateStarForm from '@/components/UpdateStarForm'

export default {
  name: 'DetailReviewUpdateForm',
  components: {
    UpdateStarForm
  },
  props:{
    review: Object,
  },
  data() {
    return {
      myReview: this.review.content,
      myRate: this.review.rate,
      modalId: `reviewUpdateModal${this.review.id}`
    }
  },
  methods: {
    ...mapActions(['fetchReviewList']),
    tokenHeader() {
      const token = localStorage.getItem('token')
      return {
        Authorization: `Token ${token}`
      }
    },
    rateSelected(rate){
      this.myRate = rate
    },
    putMyReview() {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/reviews/${this.review.id}/`,
        headers: this.tokenHeader(),
        data: {
          content: this.myReview,
          rate: this.myRate,
          movie: this.movieDetail.id,
        }
      })
        .then(() => {
          this.fetchReviewList(this.movieDetail.id)
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