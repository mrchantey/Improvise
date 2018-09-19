import Vue from 'vue'
import Router from 'vue-router'
import RawCommand from './views/command/RawCommand.vue';
import DynamicCommand from './views/command/DynamicCommand.vue';

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/index.html',
      name: 'home2',
      component: DynamicCommand
    },
    {
      path: '/',
      name: 'home',
      component: DynamicCommand
    }, {
      path: '/rawcommand',
      name: 'raw command',
      component: RawCommand
    }, {
      path: '/dynamiccommand',
      name: 'dynamic command',
      component: DynamicCommand
    }
  ]
})
