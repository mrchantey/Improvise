// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ServerInterface from './js/serverInterface.js'
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  $serverInterface: "this is a test",
  components: { App },
  template: '<App/>',
  beforeCreate() {
    window.$serverInterface = ServerInterface("http://localhost:5000", true)
  }
})

