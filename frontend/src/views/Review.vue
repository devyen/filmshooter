<template>
  <div class="container">
    <div class="row">
      <div class="offset-2 col-8">
        <h2 class="mt-5 mb-4">리뷰 & 댓글</h2>
        <detail-review-list-item v-if="review" :review="review"></detail-review-list-item>
        <review-comment-list :commentList="commentList"></review-comment-list>
      </div>
    </div>
  </div>
</template>

<script>
import DetailReviewListItem from '@/components/DetailReviewListItem'
import ReviewCommentList from '@/components/ReviewCommentList'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Review',
  components: {
    DetailReviewListItem,
    ReviewCommentList,
  },
  data() {
    return {
      reviewId: this.$route.params.reviewId,
    }
  },
  methods: {
    ...mapActions(['fetchReview'])
  },
  computed: {
    ...mapState(['review', 'commentList'])
  },
  created(){
    this.fetchReview(this.reviewId)
  }
}
</script>