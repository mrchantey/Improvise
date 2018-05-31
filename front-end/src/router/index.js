import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Connection from '@/components/connection/Connection'
import Settings from '@/components/Settings'
import Subtitles from '@/components/Subtitles'
import Actions from '@/components/actions/Actions'

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
      path: '/actions',
      name: 'Actions',
      component: Actions,

    },
    {
      path: '/subtitles',
      name: 'Subtitles',
      component: Subtitles
    }],
  mode: 'history'
})
