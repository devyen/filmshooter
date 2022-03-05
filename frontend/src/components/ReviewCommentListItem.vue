<template>
  <div class="card p-4 mb-3">
    <!-- <div class="row">
      <div class="col-6">
        <router-link :to="{ name: 'Profile', params: { nickname: comment.user.nickname } }">작성자: {{ comment.user.nickname }}</router-link>
      </div>
    </div>
    <hr> -->
    <div class="row">
      <div v-if="isCommentEdit">
        <textarea rows="3" type="text" class="form-control" v-model="myCommentContent" @keyup.enter="putComment" @blur="putComment"></textarea>
      </div>
      <div v-else>
        <p>
          <router-link class="fw-bold pe-2" :to="{ name: 'Profile', params: { nickname: comment.user.nickname } }">{{ comment.user.nickname }}</router-link>
          {{ comment.content }}
        </p>
        <hr>
        <div class="row">
          <div class="col-6">
            <p class="my-0 created-at">{{ comment.created_at }}</p>
          </div>
          <div class="text-end col-6" v-if="user.user_id === comment.user.id">
            <span class="mx-3" @click="isCommentEdit=true">
              <i class="fas fa-edit"></i>
            </span>
            <span @click="deleteComment">
              <i class="far fa-trash-alt"></i>
            </span> 
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'ReviewCommentListItem',
  props: {
    comment: Object
  },
  data() {
    return {
      myCommentContent: this.comment.content,
      isCommentEdit: false,
      reviewId: this.$route.params.reviewId,
    }
  },
  methods: {
    ...mapActions(['fetchReview']),
    tokenHeader() {
      const token = localStorage.getItem('token')
      return {
        Authorization: `Token ${token}`
      }
    },
    toggleCommentEdit() {
      this.isCommentEdit = !this.isCommentEdit
    },
    putComment() {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/reviews/comments/${this.comment.id}/`,
        headers: this.tokenHeader(),
        data: {
          review: this.reviewId,
          content: this.myCommentContent
        }
      })
        .then(() => {
          this.fetchReview(this.reviewId)
          this.isCommentEdit = false
        })
        .catch(err => console.error(err))
    },
    deleteComment() {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/reviews/comments/${this.comment.id}/`,
        headers: this.tokenHeader(),
      })
        .then(() => {
          this.fetchReview(this.reviewId)
        })
        .catch(err => console.error(err))
    }
  },
  computed: {
    ...mapState(['user'])
  }
}
</script>

<style scoped>
.card {
  background-color: #585a5c;
  border: none;
}

.created-at {
  color: #141517;
  font-size: 0.em;
}

</style>