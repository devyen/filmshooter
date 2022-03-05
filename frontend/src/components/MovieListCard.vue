<template>
  <div class="p-3">
    <router-link :to="{ name: 'Detail', params: { movieId: movie.id} }">
      <div class="imageContainer">
        <img :src="imgSrc" class="img-fluid my-0" :alt="movie.title">
      </div>
    </router-link>
    <div v-if="movie" class="img-footer row g-0 mt-1">
      <div :class="{ 'col-10': this.$route.name !== 'Profile' }">
        <p class="my-0">{{ movie.title }}</p>
        <span class="text-muted release">{{ movie.release_date.slice(0, 4) }}</span>
      </div>
      <div v-if="this.$route.name !== 'Profile'"  class="col-2 text-end mt-1">
        <span v-if="isLiked">
          <i class="fas fa-heart" @click="likeMovie"></i>
        </span>
        <span v-else>
          <span v-if="isLoggedIn">
            <i class="far fa-heart" @click="likeMovie"></i>
          </span>
          <span v-else data-bs-toggle="modal" data-bs-target="#loginSignupModal">
            <i class="far fa-heart"></i>
          </span>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'

export default {
  name: 'MovieListCard',
  props: {
    movie: Object,
  },
  data() {
    return {
      toggleLike: false,
    }
  },
  methods: {
    tokenHeader() {
      const token = localStorage.getItem('token')
      return {
        Authorization: `Token ${token}`
      }
    },
    likeMovie() {
      axios({
        method: 'post',
        url: `${this.serverHost}/movies/${this.movie.id}/like/`,
        headers: this.tokenHeader()
      })
        .then(() => {
          this.toggleLike = !this.toggleLike
        })
        .catch(err => console.error(err))
    }
  },
  computed: {
    ...mapState(['isLoggedIn', 'user', 'serverHost']),
    imgSrc() {
      return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
    },
    isLiked() {
      if (this.$route.name === 'Profile') {
        return true
      }
      return !this.toggleLike !== !this.movie.like_users.includes(this.user.user_id)
    },
  }
}
</script>

<style scoped>
  .release {
    font-size: 0.7rem;
  }

  .imageContainer:hover img {
    transform: scale(1.05);
    transition: all 0.1s linear;
  }

  .imageContainer {
    overflow: hidden;
    position: relative;
  }

  i {
    color: white;
  }

  .fas.fa-heart {
    color: #F75050;
  }

  i:hover {
    cursor: pointer;
  }

  img {
    height: 22rem;
    object-fit: cover;
    border-radius: 0;
    margin-bottom: 0.5em;
  }
  @media (max-width: 1200px) {
      img {
      height: 18rem;
    }
  }

  @media (max-width: 992px) {
      img {
      height: 14rem;
    }
  }

  @media (max-width: 768px) {
      img {
      height: 10rem;
    }
  }

</style>