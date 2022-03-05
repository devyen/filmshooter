<template>
  <div>
    <div class="modal fade" id="deleteConfirmModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p class="text-dark text-center fs-5">정말로 삭제하시겠습니까?</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
            <button type="button" class="btn btn-danger" data-bs-dismiss="modal" @click="deleteReview">삭제</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import axios from 'axios'

export default {
  name: 'DetailReviewDeleteConfirm',
  props: {
    review: Object,
  },
  methods: {
    ...mapActions(['fetchReviewList']),
    tokenHeader() {
      const token = localStorage.getItem('token')
      return {
        Authorization: `Token ${token}`
      }
    },
    deleteReview() {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/reviews/${this.review.id}`,
        headers: this.tokenHeader()
      })
        .then(() => {
          this.fetchReviewList(this.movieDetail.id)
        })
        .catch(err => console.error(err))
    },
  },
  computed: {
    ...mapState(['movieDetail'])
  }
}
</script>

<style>

</style>