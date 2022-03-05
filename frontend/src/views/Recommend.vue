<template>
  <div class="container">
    <p class="mt-5 mb-2 fs-1 text-center">
      <span class="text-primary fw-bold">{{ user.nickname }}</span>
      <span>님이 좋아할만한 영화입니다</span>
    </p>
    <recommend-movie-list
      v-for="(recommendMovies, idx) in recommendMoviesList"
      :key="idx"
      :recommendMovies="recommendMovies"
    ></recommend-movie-list>
  </div>
</template>

<script>
import axios from 'axios'
import RecommendMovieList from '@/components/RecommendMovieList'
import { mapState } from 'vuex'

export default {
  name: 'Recommend',
  components: {
    RecommendMovieList,
  },
  data() {
    return {
      recommendMoviesList: []
    }
  },
  methods: {
    tokenHeader() {
      const token = localStorage.getItem('token')
      return {
        Authorization: `Token ${token}`
      }
    },
    fetchRecommendedMovies() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/recommended/',
        headers: this.tokenHeader()
      })
        .then(res => {
          for (let i=0; i<res.data.length/6;i++) {
            const recommendMovies = res.data.slice(6 * i, 6 * i + 6)
            this.recommendMoviesList.push(recommendMovies)
          }
        })
        .catch(err => console.error(err))
    }
  },
  computed: {
    ...mapState(['user'])
  },
  created() {
    this.fetchRecommendedMovies()
  }

}
</script>

<style>

</style>