import Vue from 'vue'
import App from './App.vue'
import router from './router'
import NaoServer from "./js/NaoServer"
import CommandOptions from "./js/CommandOptions"
Vue.config.productionTip = false

new Vue({
  beforeCreate() {
    window.$ServerRequest = NaoServer.ServerRequest;
    window.$CommandOptions = CommandOptions;
    // CommandOptions.TestGetCommandOptions();
  },
  router,
  render: h => h(App)
}).$mount('#app')
