<template>
  <div>
    <review-comment-form></review-comment-form>
    <review-comment-list-item
      v-for="comment in commentList"
      :key="comment.id"
      :comment="comment"
    >
    </review-comment-list-item>
  </div>
</template>

<script>
import ReviewCommentListItem from '@/components/ReviewCommentListItem'
import ReviewCommentForm from '@/components/ReviewCommentForm'

export default {
  name: 'ReviewCommentList',
  components: {
    ReviewCommentListItem,
    ReviewCommentForm,
  },
  props: {
    commentList: Array,
  }
}
</script>

<style>

</style>