<template>
  <div class="mt-5">
    <movie-list v-for="(list, idx) in listTen" :key="idx" :list="list"></movie-list>
    <!-- <movie-list :list=listTen[0]></movie-list> -->
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    MovieList,
  },
  data() {
    return {
      
    }
  },
  methods:{
    ...mapActions(['fetchMovieList']),
  },
  computed: {
    ...mapState(['movieList']),
    listTen() {
      const result = []
      for (let i=0; i < this.movieList.length/10; i++) {
        const temp = []
        for (let j=0; j<10; j++) {
          temp.push(this.movieList[i*10 + j])
        }
        result.push(temp)
      }
      return result
    }
  },
  created() {
    this.fetchMovieList()
  }
}
</script>
