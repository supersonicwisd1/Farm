<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Add Crop</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Crop Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="cropname">
                        </div>
                    </div>

                    <div class="field">
                        <label>Category</label>
                        <div class="control">
                            <input type="text" class="input" v-model="category">
                        </div>
                    </div>

                    <div class="field">
                        <label>Quantity</label>
                        <div class="control">
                            <input type="number" class="input" v-model="quantity">
                        </div>
                    </div>

                    <div class="field">
                        <label>Price</label>
                        <div class="control">
                            <input type="number" class="input" v-model="price">
                        </div>
                    </div>

                    <div class="field">
                        <label>Description</label>
                        <div class="control">
                            <input type="text" class="input" v-model="description">
                        </div>
                    </div>

                    <div class="field">
                        <label>Discount</label>
                        <div class="control">
                            <input type="number" class="input" v-model="discount">
                        </div>
                    </div>

                    <div class="field">
                        <label for="description">Delivery Type</label>
                        <div class="control">
                            <textarea id="description" rows="4" cols="50" type="text" class="input" v-model="deliverytype"></textarea>
                        </div>
                    </div>

                    
                    <div class="field">
                        <label>Photo</label>
                        <div class="control">
                            <input type="image" class="input" v-model="image">
                        </div>
                    </div>


                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <router-link to="/profile"><button type="submit" class="button is-dark">Add</button></router-link>
                        </div>
                    </div>

                </form>
            </div>
        </div>
    </div>
</template>

<script>

export default{
    name: 'AddCrop',
    data() {
        return {
            cropname: '',
            category: '',
            description: '',
            quantity: '',
            price: '',
            discount: '',
            deliverytype: '',
            image: '',
            errors: [],
        }
    },
    mounted() {
        document.title = 'Add Crop | FARM'
    },
    methods: {
        submitForm() {
            
        }
    }
}
</script>