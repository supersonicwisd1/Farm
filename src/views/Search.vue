<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Search</h1>

                <h2 class="is-size-5 has-text-grey">Search term "{{ query }}" </h2>
            </div>

            <ProductBox
                v-for="crop in crops"
                :key="crop.id"
                :crop="crop" />
        </div>
    </div>
</template>

<script>
import axios from "axios"
import CropBox from '@/components/CropBox.vue'

export default {
    name: 'Search',
    components: {
        CropBox
    },
    data() {
        return{
            crops: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | BuyFast'

        let url = window.location.search.substring(1)
        let params = new URLSearchParams(url)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true)

            await axios
                .post('/api/v1/crops/search/', {'query': this.query})
                .then(response => {
                    this.crops = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>