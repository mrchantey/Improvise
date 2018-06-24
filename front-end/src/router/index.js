import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Dialog from '@/components/dialog/Dialog'
import Connection from '@/components/connection/Connection'
import Settings from '@/components/Settings'
import Subtitles from '@/components/Subtitles'
import Actions from '@/components/actions/Actions'
import Remote from '@/components/remote/Remote'


Vue.use(Router)


export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/remote',
      name: 'Remote',
      component: Remote
    },
    {
      path: '/connection',
      component: Connection
    },
    {
      path: '/dialog',
      component: Dialog
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
