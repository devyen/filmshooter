<template>
  <div class="col-2">
    <div class="imageContainer">
      <router-link :to="{ name: 'Detail', params: { movieId: recommendMovie.id} }">
        <img :src="imgSrc" class="img-fluid" :alt="recommendMovie.title">
        <div class="over">
          <p class="over-title">{{ recommendMovie.title }}</p>
          <p class="over-release">{{ recommendMovie.release_date }}</p>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecommendMovieItem',
  props:{
    recommendMovie: Object,
  },
  computed: {
    imgSrc() {
      return `https://image.tmdb.org/t/p/w500${this.recommendMovie.poster_path}`
    }
  }
}
</script>

<style scoped>
  img {
    height: 20rem;
    object-fit: cover;
  }

  .imageContainer:hover img {
    transform: scale(1.05);
    transition: all 0.1s linear;
  }

  .imageContainer {
    overflow: hidden;
    position: relative;
  }

  .over {
    display: none;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }

  .imageContainer:hover .over {
    display: flex;
    background-color: rgba(0, 0, 0, 0.6);
    flex-flow: column;
    color: #eee;
    text-align: center;
    padding: 0.5rem;
  }

  .over-title {
    margin-top: 5.5rem;
    font-size: 1.2rem;
    font-weight: bold;
  }

  .over-release {
    font-size: 0.8rem;
  }



  @media (max-width: 1200px) {
      img {
      height: 16rem;
    }
  }

  @media (max-width: 992px) {
      img {
      height: 12rem;
    }
  }

  @media (max-width: 768px) {
      img {
      height: 8rem;
    }
  }

</style>