<template>
  <div class="container my-5 g-0">
    <div class="row position-relative">
      <div v-if="list.length > 0">
        <carousel :items="5" :nav="false">
          <template slot="prev"><span class="prev fs-2"><i class="fas fa-chevron-left"></i></span></template>
          <movie-list-card
            v-for="movie in list"
            :key="movie.id"
            :movie="movie"
          >
          </movie-list-card>
          <template v-if="list.length > 5" slot="next"><span class="next fs-2"><i class="fas fa-chevron-right"></i></span></template>
        </carousel>
      </div>
    </div>
  </div>
</template>
<script>
import carousel from 'vue-owl-carousel'
import MovieListCard from '../components/MovieListCard'

export default {
  name: 'MovieList',
  components: {
    MovieListCard,
    carousel,
  },
  props: {
    list: Array,
  },
}
</script>

<style scoped>
i {
  color: #D6D6D6;
}

i:hover {
  background: linear-gradient(to top, #4A00E0, #8E2DE2);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.owl-carousel {
  position: relative;
}

.prev, .next {
  position: absolute;
  top: 40%;
}

.prev {
  left: -2rem;
}

.next {
  right: -2rem;
}

</style>