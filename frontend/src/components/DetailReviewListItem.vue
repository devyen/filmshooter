<template>
  <div v-if="review" class="card p-4" :class="{ 'order-first': isMyReview }">
      <div class="row">
        <div class="col-8">
          <router-link v-if="this.$route.name!=='Profile'" class="writer" :to="{ name: 'Profile', params: { nickname: review.user.nickname } }">{{ review.user.nickname }}</router-link>
          <router-link v-else class="writer" :to="{ name: 'Detail', params: { movieId: review.movie.id } }">{{ review.movie.title }}</router-link>
          <!-- <p>평점 : {{ review.rate }}</p> -->
          <div class="review-star">
            <div class="review-star-fill fs-4" :style="{ width: review.rate * 20 + 0.4 + '%' }">
              <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
            </div>
            <div class="review-star-base fs-4">
              <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
            </div>
          </div>
        </div>
        <div class="col-4 text-end date">
          <p class="my-0">
            <span class="font-dark">작성일 </span>
            <span>{{ review.created_at }}</span>
          </p>
          <p class="my-0">
            <span class="font-dark">수정일 </span>
            <span>{{ review.updated_at }}</span>
          </p>
        </div>
      </div>
      <hr>
      <p>{{ review.content }}</p>
      <hr>
      <div class="row">
        <span class="col-6">
          <span v-if="isLiked">
            <span @click="likeReview">
              <i class="fas fa-thumbs-up"></i>
            </span>
          </span>
          <span v-else>
            <span v-if="isLoggedIn" @click="likeReview">
              <i class="far fa-thumbs-up"></i>
            </span>
            <span v-else data-bs-toggle="modal" data-bs-target="#loginSignupModal">
              <i class="far fa-thumbs-up"></i>
            </span>
          </span>
          <span class="px-2">{{ likesCount }}</span>
          <router-link class="px-2" v-if="this.$route.name==='Detail'" :to="{ name: 'Review', params: { reviewId: review.id }}">
            <span>댓글 {{ review.comments_count }}개</span>
          </router-link>
        </span>
        
        <span class="col-6 text-end" v-if="isMyReview && this.$route.name === 'Detail'">
          <span class="mx-3" data-bs-toggle="modal" :data-bs-target="modalId">
            <i class="fas fa-edit"></i>
          </span>
          <span @click="deleteReview">
            <i class="far fa-trash-alt"></i>
          </span>
        </span>
      </div>
    <detail-review-update-form :review="review"></detail-review-update-form>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapState } from 'vuex'
import DetailReviewUpdateForm from '@/components/DetailReviewUpdateForm'

export default {
  name: 'DetailReviewListItem',
  props: {
    review: Object,
  },
  components:{
    DetailReviewUpdateForm
  },
  data() {
    return {
      modalId: `#reviewUpdateModal${this.review.id}`,
      likesCount: this.review.like_users_count,
      toggleLike: false,
    }
  },
  methods: {
    ...mapActions(['fetchReviewList']),
    tokenHeader() {
      const token = localStorage.getItem('token')
      return {
        Authorization: `Token ${token}`
      }
    },
    deleteReview() {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/reviews/${this.review.id}`,
        headers: this.tokenHeader()
      })
        .then(res => {
          console.log(res)
          this.fetchReviewList(this.movieDetail.id)
        })
        .catch(err => console.error(err))
    },
    likeReview() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/reviews/${this.review.id}/like/`,
        headers: this.tokenHeader()
      })
        .then(res => {
          console.log(res)
          this.likesCount = res.data.likesCount
          this.toggleLike = !this.toggleLike
        })
        .catch(err => console.error(err))
    }
  },
  computed: {
    ...mapState(['movieDetail', 'user', 'isLoggedIn',]),
    commentCount() {
      return this.review.comments ? this.review.comments.length : 0
    },
    isLiked(){
      return !this.toggleLike !== !this.review.like_users.includes(this.user.user_id)
    },
    isMyReview() {
      return this.user.user_id === this.review.user.id
    } 
  }
}
</script>

<style>
.font-dark{
  color: #aeb1b8;
}
.date {
  font-size: 0.9em;
}
.writer {
  font-size: 1.4em;
  font-weight: bold;
}
i {
  font-size: 1.4em;
}
i:hover {
  cursor: pointer;
}

.review-star {
  color: #aaa9a9; 
  position: relative;
  user-select: disable;
  /* unicode-bidi: bidi-override; */
  width: max-content;
  -webkit-text-fill-color: transparent; /*Will override color (regardless of order)*/
  -webkit-user-select: none;
}
 
.review-star-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
 
.review-star-base {
  z-index: 0;
  padding: 0;
}
</style>