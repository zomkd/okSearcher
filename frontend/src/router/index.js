import Vue from "vue"
import Router from "vue-router"
import Index from "../components/Index"
import Login from "../components/Login"
import store from "../store/index"

Vue.use(Router)

const routes = [
    {
        path: "/",
        redirect: {
            name: "login"
        }
    },
    {
        path: "/login",
        name: "login",
        component: Login,
    },
    {
        path: "/index",
        name: "index",
        component: Index,
        beforeEnter: (to, from, next) => {
            if(store.getters.AUTH == false) {
                next(false);
            } else {
                next();
            }
        }
    },
]


const router = new Router({
    mode: 'history',
    routes,
});

export default router;