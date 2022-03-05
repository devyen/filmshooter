<template>
  <div class="row py-4">
    <recommend-movie-item
      v-for="recommendMovie in recommendMovies"
      :key="recommendMovie.id"
      :recommendMovie="recommendMovie"
    ></recommend-movie-item>
  </div>
</template>

<script>
import RecommendMovieItem from '@/components/RecommendMovieItem'

export default {
  name: 'RecommendMovieList',
  props: {
    recommendMovies: Array,
  },
  components: {
    RecommendMovieItem
  }
}
</script>

<style>

</style>