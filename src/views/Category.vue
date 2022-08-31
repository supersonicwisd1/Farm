<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.title }}</h2>
            </div>

            <ProductBox
                v-for="crop in category.crops"
                :key="crop.id"
                :crop="crop" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

import CropBox from '@/components/CropBox.vue'

export default {
    name: 'Category',
    components: {
        CropBox,
    },
    data() {
        return {
            category: {
                crops: []
            }
        }
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug

            await axios
                .get(`/api/v1/crops/${category_slug}/`)
                .then(response => {
                    this.category = response.data

                    document.title = this.category.title + ' | BuyFast'
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: "Something went wrong. Please try again",
                        type: "is-danger",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>