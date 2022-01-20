import Vue from 'vue'
import App from './App.vue'
import router from "./router/index"
import VueEllipseProgress from 'vue-ellipse-progress'
import {store} from './store';
import vuetify from './plugins/vuetify'

Vue.use(VueEllipseProgress);
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  store,
  vuetify,
  router
}).$mount('#app')
