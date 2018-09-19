import Vue from 'vue'
import App from './App.vue'
import router from './router'
import CommandUtility from "./js/CommandUtility"
Vue.config.productionTip = false

new Vue({
  beforeCreate() {
    const presets = CommandUtility.GetCommandPresets();
    const command = CommandUtility.CommandBodyToCommandFields(presets[0])
    // const command = CommandUtility.CommandFieldsToCommandBody(presets[0])
    // console.log(presets[0]);
    console.log(command);
  },
  router,
  render: h => h(App)
}).$mount('#app')
