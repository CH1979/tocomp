import { Token, User } from '../../api/auth'
import {
  REFRESH_TOKEN,
  SET_API_STATUS_ERROR,
  SET_API_STATUS_UNKNOWN_ERROR,
  USER_LOGIN,
  USER_LOGOUT
} from '../mutation-types'

const state = () => ({
  user: null,
  access_token_expiration: null,
  refresh_token_expiration: null
})

const getters = {
  user: state => state.user,
  access_token_expiration: state => state.access_token_expiration,
  refresh_token_expiration: state => state.refresh_token_expiration
}

const mutations = {
  [USER_LOGIN] (state, data) {
    state.user = data.user
    state.access_token_expiration = new Date(data.access_token_expiration)
  },
  [USER_LOGOUT] (state) {
    state.user = null
  },
  [REFRESH_TOKEN] (state, data) {
    state.access_token_expiration = new Date(data.access_token_expiration)
  }
}

const actions = {
  userLogin ({ commit }, userData) {
    User.login(userData).then(
      response => {
        commit(USER_LOGIN, response.data)
      },
      error => {
        if (error.response.status === 400) {
          commit(SET_API_STATUS_ERROR, error.response.data['non_field_errors'][0])
        } else {
          commit(SET_API_STATUS_UNKNOWN_ERROR)
        }
      }
    )
  },
  userLogout ({ commit }) {
    User.logout().then(
      commit(USER_LOGOUT)
    )
  },
  userCheck ({ commit }) {
    User.info().then(
      response => {
        commit(USER_LOGIN, {'user': response.data})
      },
      error => {
        console.log(error)
        if (error.response.status === 401) {
          commit(USER_LOGOUT)
        } else {
          commit(SET_API_STATUS_UNKNOWN_ERROR)
        }
      }
    )
  },
  refreshToken ({ commit }) {
    Token.refresh().then(
      response => {
        commit(REFRESH_TOKEN, response.data)
      },
      error => {
        if (error.response.status === 401) {
          commit(USER_LOGOUT)
        } else {
          commit(SET_API_STATUS_UNKNOWN_ERROR)
        }
      }
    )
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
