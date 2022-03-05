<template>
  <div>
    <div class="backdropContainer">
      <img class="backdropImage" :src="imgBackdropSrc" :alt="movieDetail.title">
    </div>
    <div class="container">
      <div class="dimmedLayer">
      </div>
      <div class="offset-1 col-10">
        <div class="row py-5">
          <img class="offset-1 col-4 img-fluid px-4" :src="imgSrc" :alt="movieDetail.title">
          <article class="col-6">
            <div class="fs-2 fw-bold mb-2">
              {{ movieDetail.title }}
            </div>
            <span v-for="(genre, idx) in genres" :key="idx">{{ genre }} ・ </span>
            <span>{{ movieDetail.runtime }}분</span>
            <p class="mb-1">{{ movieDetail.release_date }}</p>
            <div class="d-flex justify-content-end align-items-center">
              <span class="d-flex align-items-center fs-4 mx-3" v-if="!isReviewed" data-bs-toggle="modal" :data-bs-target="modalId">
                <span class="small-text p-2">평가하기</span>
                <i class="fas fa-pen-nib"></i>
              </span>
              <span v-if="isLiked" class="fs-4">
                <i class="fas fa-heart" @click="likeMovie"></i>
              </span>
              <span v-else class="fs-4">
                <span v-if="isLoggedIn">
                  <i class="far fa-heart" @click="likeMovie"></i>
                </span>
                <span v-else data-bs-toggle="modal" data-bs-target="#loginSignupModal" class="fs-3">
                  <i class="far fa-heart"></i>
                </span>
              </span>
            </div>
            <p class="overview">{{ movieDetail.overview }}</p>
          </article>
        </div>
        <movie-detail-review-form></movie-detail-review-form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
import MovieDetailReviewForm from '@/components/MovieDetailReviewForm'

export default {
  name:'MovieDetail',
  data() {
    return {
      serverHost: 'http://127.0.0.1:8000',
      toggleLike: false,
    }
  },
  props:{
    movieDetail: Object,
    reviewList: Array,
  },
  components: {
    MovieDetailReviewForm,
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
        url: `${this.serverHost}/movies/${this.movieDetail.id}/like/`,
        headers: this.tokenHeader()
      })
        .then(() => {
          this.toggleLike = !this.toggleLike
          
        })
        .catch(err => console.error(err))
    }
  },
  computed:{
    ...mapState(['isLoggedIn', 'user']),
    imgSrc() {
      return `https://image.tmdb.org/t/p/w780${this.movieDetail.poster_path}`
    },
    imgBackdropSrc() {
      if (this.movieDetail.backdrop_path) {
        return `https://image.tmdb.org/t/p/w1280${this.movieDetail.backdrop_path}`
      } else {
        return this.imgSrc
      }
    },
    isLiked() {
      if (!this.movieDetail.like_users) {
        return []
      }
      return !this.toggleLike !== !this.movieDetail.like_users.includes(this.user.user_id)
    },
    genres() {
      const genres = []
      if (!this.movieDetail.genres) {
        return []
      }
      this.movieDetail.genres.forEach(genre => {
         genres.push(genre.name)
      })
      return genres
    },
    isReviewed() {
      return this.reviewList.some(review => review.user.id === this.user.user_id)
    },
    modalId() {
      return this.isLoggedIn ? '#reviewCreateModal' : '#loginSignupModal'
    },
  },
}
</script>

<style scoped>
.small-text {
  font-size: 0.6em;
}
.backdropImage {
  position: relative;
  top: auto;
  right: auto;
  width: 100%;
  height: 25rem;
  object-fit: cover;
}

.dimmedLayer {
  position: absolute;
  top: 0;
  left: 0;
  background-image: 
  linear-gradient(180deg,rgba(20,20,20,0.3) 1%,rgba(20,20,20,0.5) 70%,#141414 98% );
  width: 100%;
  height: 25rem;
  overflow: hidden;
}

.i {
  color: white;
}

.fas.fa-heart {
  color: #F75050;
}

i:hover {
  transform: scale(1.1);
  cursor: pointer;
}

.overview {
  margin-top: 1.5em;
  font-weight: 300;
  font-size: 1.1em;

}

</style>