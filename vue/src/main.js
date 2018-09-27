import Vue from 'vue'
import App from './App.vue'
import router from './router'
// import EventPoller from './js/EventPoller'


Vue.config.productionTip = false



new Vue({
  beforeCreate() {
    // EventPoller.BeginSpokenPhrasePolling()

  },
  router,
  render: h => h(App)
}).$mount('#app')
