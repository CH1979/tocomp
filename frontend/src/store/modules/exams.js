import { Exam } from '../../api/exams'
import {
  CREATE_EXAM,
  DELETE_EXAM,
  SET_API_STATUS_ERROR,
  SET_EXAMS,
  SET_API_STATUS_UNKNOWN_ERROR
} from '../mutation-types'

const state = () => ({
  exams: []
})

const getters = {
  exams: state => state.exams
}

const mutations = {
  [CREATE_EXAM] (state, exam) {
    state.exams = [...state.exams, exam]
  },
  [DELETE_EXAM] (state, { id }) {
    state.exams = state.exams.filter(exam => {
      return exam.id !== id
    })
  },
  [SET_EXAMS] (state, { exams }) {
    state.exams = exams
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
          commit(SET_API_STATUS_UNKNOWN_ERROR)
        }
      }
    )
  },
  deleteExam ({commit}, exam) {
    Exam.delete(exam)
      .then(
        response => {
          commit(DELETE_EXAM, exam)
        },
        error => {
          if (error.response.status === 400) {
            commit(SET_API_STATUS_ERROR, error.response.data['message'])
          } else {
            commit(SET_API_STATUS_UNKNOWN_ERROR)
          }
        }
      )
  },
  getExams ({ commit }) {
    Exam.list().then(exams => {
      commit(SET_EXAMS, { exams })
    })
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
