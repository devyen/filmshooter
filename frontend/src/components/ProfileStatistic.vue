<template>
  <div>
    <div class="card my-4">
      <h3 class="m-4">통계</h3>
      <ul class="ul mb-5">
        <li class="statistic-li">
          <div class="stat-num">{{ statistic.reviewsCount }}</div>
          <div>평가</div>
        </li>
        <li class="statistic-li">
          <div class="stat-num">{{ statistic.movieLikesCount }}</div>
          <div>좋아요 누른 영화</div>
        </li>
        <li class="statistic-li">
          <div class="stat-num">{{ Math.round(statistic.rateAvg * 10) / 10 }}</div>
          <div>별점 평균</div>
        </li>
      </ul>
    </div>
    <div class="card px-4">
      <h4 class="mt-4">높은 평점을 준 영화</h4>
      <!-- <movie-list v-for="(list, idx) in topRankMovies" :key="idx" :list="list"></movie-list> -->
      <!-- <movie-list :topRankMovies="topRankMovies"></movie-list> -->
      <movie-list :list="topRankMovies"></movie-list>
    </div>
    <div class="card my-4 px-4">
      <!-- <movie-list :list="likeMovies"></movie-list> -->
      <h4 class="mt-4">좋아요 누른 영화</h4>
      <movie-list :list="likeMovies"></movie-list>
    </div>
    <div class="card my-4">
      <h4 class="mx-4 mt-4">내가 쓴 리뷰</h4>
      <detail-review-list :reviewList="reviews"></detail-review-list>
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
import DetailReviewList from '@/components/DetailReviewList'
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name: 'ProfileStatistic',
  components: {
    MovieList,
    DetailReviewList
  },
  props:{
    profile: Object,
    nickname: String,
  },
  data() {
    return {
      statistic: {},
      reviews: [],
      topRankReviews: [],
      topRankMovies: [],
      likeMovies: [],
    }
  },
  methods: {
    fetchStatistic() {
      axios({
        method: 'get',
        url: this.serverHost + `/accounts/${this.nickname}/statistic/`
      })
        .then(res => {
          // console.log(res.data)
          this.statistic = res.data
        })
    },
    fetchReviews() {
      axios({
        method: 'get',
        url: this.serverHost + `/accounts/${this.nickname}/reviews/`
      })
        .then(res => {
          this.reviews = res.data
        })
    },
    fetchTopRankReviews() {
      axios({
        method: 'get',
        url: this.serverHost + `/accounts/${this.nickname}/toprank_reviews/`
      })
        .then(res => {
          this.topRankReviews = res.data
          this.topRankReviews.forEach(review => {
            this.topRankMovies.push(review.movie)
          })
        })
    },
    fetchLikeMovies() {
      axios({
        method: 'get',
        url: this.serverHost + `/accounts/${this.nickname}/like_movies/`
      })
        .then(res => {
          this.likeMovies = res.data 
          // this.likeMovies = res.data 
        })
    },
    // 위 4개 methods 한번에 실행하는 method
    fetchProfile() {
      this.fetchStatistic()
      this.fetchReviews()
      this.fetchTopRankReviews()
      this.fetchLikeMovies()
    },
  },
  computed: {
    ...mapState(['serverHost']),
  },
  created() {
    this.fetchProfile()
  }
}
</script>

<style>
.ul {
  list-style: none;
  padding: 0;
  margin: 0;
  margin: 0 -6px;
}
.statistic-li {
  display: inline-block;
  vertical-align: top;
  text-align: center;
  box-sizing: border-box;
  width: 33.33333333333333%;
  padding: 0 6px;
}
.stat-num {
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -0.5px;
  line-height: 19px;
  margin: 0 0 4px;
}
</style>