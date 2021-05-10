import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import exams from './modules/exams'
import { Examcard } from '../api/examcards'
import { Question } from '../api/questions'
import {
  CREATE_QUESTION,
  CREATE_EXAMCARD,
  DELETE_EXAMCARD,
  DELETE_QUESTION,
  SET_EXAMCARDDETAIL,
  SET_API_STATUS_ERROR,
  SET_API_STATUS_DEFAULT
} from './mutation-types'

Vue.use(Vuex)

const state = {
  apiError: false,
  errorMessage: '',
  examcarddetail: [],
  labels: []
}

const getters = {
  apiError: state => state.apiError,
  errorMessage: state => state.errorMessage,
  examcarddetail: state => state.examcarddetail,
  labels: state => state.labels
}

const mutations = {
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
  getExamcarddetail ({ commit }, examcard) {
    Examcard.list(examcard).then(
      examcarddetail => {
        commit(SET_EXAMCARDDETAIL, { examcarddetail })
      }
    )
  }
}

export default new Vuex.Store({
  modules: {
    exams
  },
  state,
  getters,
  actions,
  mutations
})
