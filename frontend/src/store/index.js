import Vue from 'vue'
import Vuex from 'vuex'
import exams from './modules/exams'
import examcards from './modules/examcards'
import {
  SET_API_STATUS_ERROR,
  SET_API_STATUS_DEFAULT
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
  }
}

export default new Vuex.Store({
  modules: {
    exams,
    examcards
  },
  state,
  getters,
  mutations
})
