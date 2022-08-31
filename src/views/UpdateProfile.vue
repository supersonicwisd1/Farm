<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Update Profile</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Farmer's Full Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="name">
                        </div>
                    </div>

                    <div class="field">
                        <label>E-mail</label>
                        <div class="control">
                            <input type="email" class="input" v-model="email">
                        </div>
                    </div>

                    <div class="field">
                        <label>Phone</label>
                        <div class="control">
                            <input type="tel" class="input" v-model="phone">
                        </div>
                    </div>

                    <div class="field">
                        <label>State of Origin</label>
                        <div class="control">
                            <input type="text" class="input" v-model="stateoforigin">
                        </div>
                    </div>

                    <div class="field">
                        <label>Country of Origin</label>
                        <div class="control">
                            <input type="text" class="input" v-model="countryoforigin">
                        </div>
                    </div>

                    <div class="field">
                        <label>Type of Farming</label>
                        <div class="control">
                            <input type="text" class="input" v-model="farmingtype">
                        </div>
                    </div>

                    <div class="field">
                        <label>About</label>
                        <div class="control">
                            <input type="text" class="input" v-model="about">
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
                            <router-link to="/profile"><button type="submit" class="button is-dark">Update</button></router-link>
                        </div>
                    </div>

                </form>
            </div>
        </div>
    </div>
</template>

<script>

export default{
    name: 'UpdateProfile',
    data() {
        return {
            name: '',
            email: '',
            phone: '',
            stateoforigin: '',
            countryoforigin: '',
            farmingtype: '',
            about: '',
            image: '',
            errors: [],
        }
    },
    mounted() {
        document.title = 'Update Profile | FARM'
    },
    methods: {
        submitForm() {
            
        }
    }
}
</script>