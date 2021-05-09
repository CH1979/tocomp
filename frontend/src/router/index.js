import Vue from 'vue'
import Router from 'vue-router'
import ExamList from '../components/ExamList'
import ExamDetail from '../components/ExamDetail'
import ExamcardDetail from '../components/ExamcardDetail'
import LabelList from '../components/LabelList'

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
    },
    {
      path: '/test',
      name: 'Test',
      component: LabelList,
      props: {labels: [
        {'text': '1234', 'is_correct': false},
        {'text': '7890', 'is_correct': true}
      ],
      is_many: true
      }
    }
  ]
})
