<template>
  <div class="offset-2 col-8">
    <hr class="mb-4">
    <div class="row gx-0 gy-4">
      <detail-review-list-item
        v-for="review in reviewList"
        :key="review.id"
        :review="review"
      >
      </detail-review-list-item>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import DetailReviewListItem from '@/components/DetailReviewListItem'

export default {
  name: 'DetailReviewList',
  components:{
    DetailReviewListItem,
  },
  props: {
    reviewList: Array,
  },
  data() {
    return {
    }
  },
  methods: {
  },
  computed: {
    ...mapState(['isLoggedIn', 'user']),
  },
}
</script>

<style>

</style>