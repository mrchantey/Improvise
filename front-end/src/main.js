// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import naoInterface from './js/naoInterface.js'
// import webSpeechInterface from './js/webSpeechInterface.js'
import DialogInterface from './js/dialogInterface.js'
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  // $serverInterface: "this is a test",
  components: { App },
  template: '<App/>',
  beforeCreate() {
    //needs to change to naoInterface
    const serverAddress = sessionStorage['serverAddress']
    if (serverAddress) {
      window.$apiInterface = naoInterface(serverAddress, true)
      window.$webSpeechInterface = DialogInterface(serverAddress)
    } else {
      console.log('server address not yet set')
    }



    //TEST ADD

  }
})

