import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import HomeView from '../views/HomeView.vue'

import Crop from '../views/Crop.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import Profile from '../views/Profile.vue'
import UpdateProfile from '../views/UpdateProfile.vue'
import AddCrop from '../views/AddCrop.vue'

const routes = [{
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUp
    },
    {
        path: '/log-in',
        name: 'Login',
        component: Login
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/update-profile',
        name: 'UpdateProfile',
        component: UpdateProfile,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/add-crop',
        name: 'AddCrop',
        component: AddCrop,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/search',
        name: 'Search',
        component: Search
    },
    {
        path: '/:category_slug/:crop_slug',
        name: 'Crop',
        component: Crop
    },
    {
        path: '/:category_slug',
        name: 'Category',
        component: Category
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
        next({ name: 'Login', query: { to: to.path } });
    } else {
        next()
    }
})

export default router