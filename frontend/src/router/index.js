import Vue from 'vue'
import Router from 'vue-router'

import ExamList from '../components/ExamList'
import ExamDetail from '../components/ExamDetail'
import ExamcardDetail from '../components/ExamcardDetail'
import CreateNews from '../components/CreateNews'
import News from '../components/News'
import Account from '../components/Account'
import Login from '../components/Login'
import Logout from '../components/Logout'

/* import store from '../store/index'

const redirectLogout = (to, from, next) => {
  store.dispatch('userLogout')
    .then(() => next('/'))
} */

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: { template: '<h1>Главная</h1>' }
    },
    {
      path: '/exams',
      component: ExamList
    },
    {
      path: '/exams/:id/detail',
      component: ExamDetail
    },
    {
      path: '/examcards/:id/detail',
      component: ExamcardDetail
    },
    {
      path: '/news',
      name: 'news',
      component: News
    },
    {
      path: '/news/add',
      component: CreateNews
    },
    {
      path: '/account',
      component: Account
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/logout',
      component: Logout
    }
  ]
})
