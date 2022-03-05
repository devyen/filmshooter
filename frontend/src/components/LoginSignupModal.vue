<template>
  <div class="modal" id="loginSignupModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body container-fluid">
          <p class="offset-2 col-8 text-center py-3 text-dark fs-5">로그인이 필요한 기능입니다. 지금 회원가입 또는 로그인을 하고 글을 남겨주세요!</p>
          <button type="button" class="btn btn-primary offset-2 col-8 my-2 text-white" data-bs-toggle="modal" data-bs-target="#signupModal" data-bs-dismiss="modal">회원가입</button>
          <button type="button" class="btn btn-white offset-2 col-8 text-primary" data-bs-toggle="modal" data-bs-target="#loginModal" data-bs-dismiss="modal">로그인</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginSignupModal',

}
</script>

<style>

</style>