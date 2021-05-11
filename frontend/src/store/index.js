import Vue from 'vue'
import Vuex from 'vuex'
import exams from './modules/exams'
import examcards from './modules/examcards'
import news from './modules/news'
import {
  SET_API_STATUS_ERROR,
  SET_API_STATUS_DEFAULT,
  SET_API_STATUS_UNKNOWN_ERROR
} from './mutation-types'

Vue.use(Vuex)

const state = {
  apiError: false,
  errorMessage: ''
}

const getters = {
  apiError: state => state.apiError,
  errorMessage: state => state.errorMessage
}

const mutations = {
  [SET_API_STATUS_DEFAULT] (state) {
    state.apiError = false
    state.errorMessage = ''
  },
  [SET_API_STATUS_ERROR] (state, errorMessage) {
    state.apiError = true
    state.errorMessage = errorMessage
  },
  [SET_API_STATUS_UNKNOWN_ERROR] (state, errorMessage) {
    state.apiError = true
    state.errorMessage = 'Произошла непредвиденная ошибка.' +
    'При её повторении обратитесь к адиминистратору сайта.'
  }
}

export default new Vuex.Store({
  modules: {
    exams,
    examcards,
    news
  },
  state,
  getters,
  mutations
})
