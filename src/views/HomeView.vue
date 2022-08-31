<template>
<div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to FARM
        </p>
        <p class="subtitle">
          Where farm goes digital
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Crops</h2>
      </div>

      <CropBox
        v-for="crop in Crops"
        :key="crop.id"
        :crop="crop" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import CropBox from '@/components/CropBox.vue'

export default {
  name: 'HomeView',
  data() {
    return {
      Crops: []
    }
  },
  components: {
    CropBox,
  },
  mounted() {
    this.getCrops()

    document.title = 'Home | FARM'
  },
  methods: {
    async getCrops() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/crops/')
        .then(response => {
          this.Crops = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
.hero{
  height: 50vh;
  /* background-color: black; */
  margin-top: -50px !important;
  margin-left: -50px;
  margin-right: -50px;
}
</style>