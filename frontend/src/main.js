import Vue from 'vue'
import App from './App.vue'

import "bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"

import { library } from '@fortawesome/fontawesome-svg-core'
import { faGithub } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faGithub)

Vue.config.productionTip = false
Vue.component('font-awesome-icon', FontAwesomeIcon)

new Vue({
    render: h => h(App),
}).$mount('#app')
