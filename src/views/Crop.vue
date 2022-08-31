<template>
    <div class="page-product">
        <div class="columns is multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img :src="crop.get_image">
                </figure>

                <h1 class="title">{{ crop.name }}</h1>

                <p>{{ crop.description }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Information</h2>

                <p><strong>Price per crop:</strong>${{ crop.price }}</p>
                <p><strong>Available Quantity:</strong>${{ crop.quantity }}</p>
            </div>
        </div>
    </div>
                
</template>

<script>
import axios from 'axios'

export default {
    name: 'Crop',
    data() {
        return {
            crop: {},
        }
    },
    mounted() {
        this.getCrop()
    },
    methods: {
        getCrop() {
            const category_slug = this.$route.params.category_slug
            const crop_slug = this.$route.params.crop_slug

            axios
                .get(`/api/v1/crops/${category_slug}/${crop_slug}`)
                .then(response => {
                    this.crop = response.data

                    document.title = this.crop.name + ' | BuyFast'
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>