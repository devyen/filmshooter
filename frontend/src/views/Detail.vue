<template>
  <div class="detail">
    <div class="row g-0">
      <movie-detail :movieDetail="movieDetail" :reviewList="reviewList"></movie-detail>
      <detail-review-list :reviewList="reviewList"></detail-review-list>
    </div>
  </div>
</template>

<script>
import MovieDetail from '../components/MovieDetail'
import DetailReviewList from '@/components/DetailReviewList'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'Detail',
  components: {
    MovieDetail,
    DetailReviewList,
  },
  methods: {
    ...mapActions(['fetchMovieDetail', 'fetchReviewList']),
  },
  computed: {
    ...mapState(['reviewList', 'movieDetail'])
  },
  created() {
    this.fetchMovieDetail(this.$route.params.movieId)
    this.fetchReviewList(this.$route.params.movieId)
  }
}
</script>
