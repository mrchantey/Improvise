import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import HelloWorld from '@/components/HelloWorld'
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
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
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
