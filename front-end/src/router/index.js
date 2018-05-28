import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Connection from '@/components/Connection'
import Settings from '@/components/Settings'
import SocketView from '@/components/Socket'
import Subtitles from '@/components/Subtitles'

Vue.use(Router)


export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/connection',
      component: Connection
    },
    {
      path: '/settings',
      component: Settings
    },
    {
      path: '/socket/:naoIP',
      name: 'SocketView',
      component: SocketView,

    },
    {
      path: '/subtitles',
      name: 'Subtitles',
      component: Subtitles
    }],
  mode: 'history'
})
