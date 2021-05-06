import Vue from 'vue'
import Router from 'vue-router'
import ExamList from '../components/ExamList'
import ExamDetail from '../components/ExamDetail'
import ExamcardDetail from '../components/ExamcardDetail'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: { template: '<h1>Главная</h1>' }
    },
    {
      path: '/exams',
      name: 'ExamList',
      component: ExamList
    },
    {
      path: '/exams/:id/detail',
      name: 'ExamDetail',
      component: ExamDetail
    },
    {
      path: '/examcards/:id/detail',
      name: 'ExamcardDetail',
      component: ExamcardDetail
    }
  ]
})
