import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import { Exam } from '../api/exams'
import { Examcard } from '../api/examcards'
import { Question } from '../api/questions'
import {
  CREATE_EXAM,
  CREATE_QUESTION,
  CREATE_EXAMCARD,
  DELETE_EXAM,
  DELETE_EXAMCARD,
  DELETE_QUESTION,
  SET_EXAMS,
  SET_EXAMDETAIL,
  SET_EXAMCARDDETAIL,
  SET_API_STATUS_ERROR,
  SET_API_STATUS_DEFAULT
} from './mutation-types'

Vue.use(Vuex)

const state = {
  apiError: false,
  errorMessage: '',
  exams: [],
  examdetail: [],
  examcarddetail: [],
  labels: []
}

const getters = {
  apiError: state => state.apiError,
  errorMessage: state => state.errorMessage,
  exams: state => state.exams,
  examdetail: state => state.examdetail,
  examcarddetail: state => state.examcarddetail,
  labels: state => state.labels
}

const mutations = {
  [CREATE_EXAM] (state, exam) {
    state.exams = [...state.exams, exam]
  },
  [CREATE_EXAMCARD] (state, examcard) {
    state.examdetail['examcards'] = [
      ...state.examdetail['examcards'],
      examcard
    ]
  },
  [CREATE_QUESTION] (state, question) {
    state.examcarddetail['questions'] = [
      ...state.examcarddetail['questions'],
      question
    ]
  },
  [DELETE_EXAM] (state, { id }) {
    state.exams = state.exams.filter(exam => {
      return exam.id !== id
    })
  },
  [DELETE_EXAMCARD] (state, id) {
    state.examdetail['examcards'] = state.examdetail['examcards'].filter(examcard => {
      return examcard.id !== id
    })
  },
  [DELETE_QUESTION] (state, id) {
    state.examcarddetail['questions'] = state.examcarddetail['questions'].filter(question => {
      return question.id !== id
    })
  },
  [SET_EXAMS] (state, { exams }) {
    state.exams = exams
  },
  [SET_EXAMDETAIL] (state, { examdetail }) {
    state.examdetail = examdetail
  },
  [SET_EXAMCARDDETAIL] (state, { examcarddetail }) {
    state.examcarddetail = examcarddetail
  },
  [SET_API_STATUS_DEFAULT] (state) {
    state.apiError = false
    state.errorMessage = ''
  },
  [SET_API_STATUS_ERROR] (state, errorMessage) {
    state.apiError = true
    state.errorMessage = errorMessage
  }
}

const actions = {
  createExam ({ commit }, examData) {
    Exam.create(examData).then(
      response => {
        commit(CREATE_EXAM, response.data)
      },
      error => {
        if (error.response.status === 400) {
          commit(SET_API_STATUS_ERROR, error.response.data['theme'][0])
        } else {
          commit(SET_API_STATUS_ERROR, 'Error')
        }
      }
    )
  },
  createExamcard ({ commit }, examcardData) {
    Examcard.create(examcardData).then(
      response => {
        commit(CREATE_EXAMCARD, response.data)
        router.push(`/examcards/${response.data['id']}/detail`)
      },
      error => {
        if (error.response.status === 400) {
          commit(SET_API_STATUS_ERROR, 'В данном экзамене есть билет с таким номером')
        } else {
          commit(SET_API_STATUS_ERROR, 'Error')
        }
      }
    )
  },
  createQuestion ({ commit }, questionData) {
    Question.create(questionData).then(
      response => {
        commit(CREATE_QUESTION, response.data)
      },
      error => {
        if (error.response.status === 400) {
          commit(SET_API_STATUS_ERROR, error.response.data['title'][0])
        } else {
          commit(SET_API_STATUS_ERROR, 'Error')
        }
      }
    )
  },
  deleteExam ({commit}, exam) {
    Exam.delete(exam)
      .then(response => {
        commit(DELETE_EXAM, exam)
      },
      error => {
        if (error.response.status === 400) {
          commit(SET_API_STATUS_ERROR, error.response.data['message'])
        } else {
          commit(SET_API_STATUS_ERROR, 'Error')
        }
      })
  },
  deleteExamcard ({commit}, id) {
    Examcard.delete(id)
      .then(response => {
        commit(DELETE_EXAMCARD, id)
      },
      error => {
        if (error.response.status === 400) {
          commit(SET_API_STATUS_ERROR, error.response.data['message'])
        } else {
          commit(SET_API_STATUS_ERROR, 'Error')
        }
      })
  },
  deleteQuestion ({ commit }, questionId) {
    Question.delete(questionId).then(
      commit(DELETE_QUESTION, questionId)
    )
  },
  getExams ({ commit }) {
    Exam.list().then(exams => {
      commit(SET_EXAMS, { exams })
    })
  },
  getExamdetail ({ commit }, exam) {
    Exam.detail(exam).then(
      examdetail => {
        commit(SET_EXAMDETAIL, { examdetail })
      }
    )
  },
  getExamcarddetail ({ commit }, examcard) {
    Examcard.list(examcard).then(
      examcarddetail => {
        commit(SET_EXAMCARDDETAIL, { examcarddetail })
      }
    )
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
