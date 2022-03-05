<template>
  <div>
    <div class="star-rating">
      <input type="radio" name="star" title="star" id="5-star-even" @input="onSelect">
      <label for="5-star-even">
        <img :src="emptyRightImgSrc" alt="rating star 5">
      </label>
      <input type="radio" name="star" title="star" id="5-star-odd" @input="onSelect">
      <label for="5-star-odd">
        <img :src="emptyLeftImgSrc" alt="rating star 4.5">
      </label>
      <input type="radio" name="star" title="star" id="4-star-even" @input="onSelect">
      <label for="4-star-even">
        <img :src="emptyRightImgSrc" alt="rating star 4">
      </label>
      <input type="radio" name="star" title="star" id="4-star-odd" @input="onSelect">
      <label for="4-star-odd">
        <img :src="emptyLeftImgSrc" alt="rating star 3.5">
      </label>
      <input type="radio" name="star" title="star" id="3-star-even" @input="onSelect">
      <label for="3-star-even">
        <img :src="emptyRightImgSrc" alt="rating star 3">
      </label>
      <input type="radio" name="star" title="star" id="3-star-odd" @input="onSelect">
      <label for="3-star-odd">
        <img :src="emptyLeftImgSrc" alt="rating star 2.5">
      </label>
      <input type="radio" name="star" title="star" id="2-star-even" @input="onSelect">
      <label for="2-star-even">
        <img :src="emptyRightImgSrc" alt="rating star 2">
      </label>
      <input type="radio" name="star" title="star" id="2-star-odd" @input="onSelect">
      <label for="2-star-odd">
        <img :src="emptyLeftImgSrc" alt="rating star 1.5">
      </label>
      <input type="radio" name="star" title="star" id="1-star-even" @input="onSelect">
      <label for="1-star-even">
        <img :src="emptyRightImgSrc" alt="rating star 1">
      </label>
      <input type="radio" name="star" title="star" id="1-star-odd" @input="onSelect">
      <label for="1-star-odd">
        <img :src="emptyLeftImgSrc" alt="rating star 0.5">
      </label>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StarForm',
  data() {
    return {
      emptyLeftImgSrc: require('@/assets/left_empty.png'),
      emptyRightImgSrc: require('@/assets/right_empty.png'),
      fullLeftImgSrc: require('@/assets/left_full.png'),
      fullRightImgSrc: require('@/assets/right_full.png'),
    }
  },
  methods: {
    emptyStar() {
      const allStars = document.querySelectorAll('.modal.show .star-rating > label')
      allStars.forEach(label => {
        if (label.htmlFor.includes('odd')) {
          label.children[0].src = this.emptyLeftImgSrc
        } else {
          label.children[0].src = this.emptyRightImgSrc
        }
      })
    },
    onSelect(event) {
      this.emptyStar()
      const fillStars = document.querySelectorAll('.modal.show .star-rating :checked ~ label')
      fillStars.forEach((label) => {
        if (label.htmlFor.includes('odd')) {
          label.children[0].src = this.fullLeftImgSrc
        } else {
          label.children[0].src = this.fullRightImgSrc
        }
      })
      let rate = event.target.id[0] * 1
      rate = event.target.id.includes('even') ? rate : rate - 0.5
      this.$emit('rate-selected', rate)
    }
  },
}
</script>

<style scoped>
  .star-rating{
    display:flex;
    flex-direction: row-reverse;
  }
  img {
    width: 1rem;
  }
  input {
    display:none;
  }
  .star-rating label:hover {
    cursor: pointer;
  }
</style>