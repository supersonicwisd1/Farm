<template>
  <div id="wrapper">
    <nav class="navbar is-success">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item" href="{% url 'home' %}">
              <span class="icon"><i class="fas fa-f fa-2x"></i></span>
              <span class="icon"><i class="fas fa-a fa-2x"></i></span>
              <span class="icon"><i class="fas fa-r fa-2x"></i></span>
              <span class="icon"><i class="fas fa-m fa-2x"></i></span>
            </router-link>

            <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="main-navbar" @click="showMobileMenu = !showMobileMenu">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div id='main-navbar' class="navbar-menu" :class="{'is-active': showMobileMenu }">
            <div class="navbar-start">
              <div class="navbar-item">
                  <form method="get" action="{% url 'search' %}">
                      <div class="field has-addons">
                          <div class="control">
                              <input tyoe="text" class="input" placeholder="Search..." name="query">
                          </div>
                          <div class="control">
                              <button class="button is-dark"><i class="fas fa-search"></i></button>
                          </div>
                      </div>
                  </form>
              </div>
            </div>

            <div class="navbar-end"> 
                <router-link to="/cash-crop" class="navbar-item">Cash Crop</router-link>
                <router-link to="/vegetables" class="navbar-item">Vegetables</router-link>

                <div class="navbar-item">
                    <div class="buttons">
                      <template v-if="$store.state.isAuthenticated">
                        <router-link to="/profile" class="button is-dark">
                          <span class="icon"><i class="fas fa-user"></i></span>
                          <span>Profile</span>
                        </router-link>

                        <button @click="logout()" class="button is-danger">
                          <span class="icon"><i class="fas fa-sign-out"></i></span>
                          <span>Log out</span>
                        </button>
                      </template>

                      <template v-else>
                        <router-link to="/log-in" class="button is-grey">
                          <span class="icon"><i class="fas fa-sign-in"></i></span>
                          <span>Log in</span>
                        </router-link>

                        <router-link to="/sign-up" class="button is-dark">
                          <span class="icon"><i class="fas fa-users"></i></span>
                          <span>Sign Up</span>
                        </router-link>
                      </template>
                  
                    </div>
                </div>
            </div>
        </div>
      </nav>

      <div class="is-loading-bar has-text-centered" :class="{'is-loading': $store.state.isLoading }">
        <div class="lds-dual-ring"></div>
      </div>

      <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2022</p>
    </footer>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token" + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}
</script> 

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lsd-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring{
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
