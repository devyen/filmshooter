import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLoggedIn: false,
    user: {
      user_id: null,
      username: null,
      nickname: null,
    },
    movieList: [],   // 전체 영화 리스트
    movieDetail: {}, // 단일 영화 디테일
    reviewList: [],  // 단일 영화 리뷰 리스트
    review: null,    // 단일 리뷰
    commentList: [], // 리뷰 코멘트 리스트
    serverHost: 'http://127.0.0.1:8000',
  },
  mutations: {
    SET_MOVIE_LIST(state, movieList) {
      state.movieList = movieList
    },
    SET_MOVIE_DETAIL(state, movieDetail) {
      state.movieDetail = movieDetail
    },
    SET_REVIEW_LIST(state, reviewList) {
      state.reviewList = reviewList
    },
    SET_REVIEW(state, review) {
      state.review = review
    },
    SET_COMMENT_LIST(state, commentList) {
      state.commentList = commentList
    },
    LOGIN(state, user) {
      state.isLoggedIn = true
      state.user = user
    },
    LOGOUT(state) {
      state.isLoggedIn = false
      state.user = {
        user_id: null,
        username: null,
        nickname: null,
      }
    }
  },
  actions: {
    fetchMovieList({ state, commit }) {
      axios({
        method: 'get',
        url: `${state.serverHost}/movies/`,
      })
        .then(res => {
          commit('SET_MOVIE_LIST', res.data)
        })
        .catch(err => console.error(err))
    },
    fetchMovieDetail({ state, commit }, movieId) {
      axios({
        method: 'get',
        url: `${state.serverHost}/movies/${movieId}/`,
      })
        .then(res => {
          commit('SET_MOVIE_DETAIL', res.data)
        })
        .catch(err => console.error(err))
    },
    fetchReviewList({ state, commit }, movieId) {
      axios({
        method: 'get',
        url: `${state.serverHost}/reviews/movie/${movieId}/`,
      })
        .then(res => {
          commit('SET_REVIEW_LIST', res.data)
        })
        .catch(err => console.error(err))
    },
    fetchReview({ state, commit }, reviewId) {
      axios({
        method: 'get',
        url: `${state.serverHost}/reviews/${reviewId}/`,
      })
        .then(res => {
          commit('SET_REVIEW', res.data),
          commit('SET_COMMENT_LIST', res.data.comments)
        })
        .catch(err => console.error(err))
    },
    loginAction({ commit }, user) {
      commit('LOGIN', user)
    },
    logoutAction({ commit }) {
      commit('LOGOUT')
    }
  },
  modules: {
  }
})
