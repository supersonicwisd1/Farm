<template>
    <div class="column is-3">
        
        <div class="box">
          <figure class="image is-4by3 mb-4">
            <img v-bind:src="crop.get_thumbnail">
          </figure>

          <h3 class="is-size-4">{{ crop.name }}</h3>
          <p class="is-size-6 mb-5 has-text-grey">${{ crop.price }}</p>

          <router-link :to="product.get_absolute_url" class="button is-dark mt-4">View details</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CropBox',
    props: {
        crop: Object
    }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>
