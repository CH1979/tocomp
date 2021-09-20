import router from '../../router'
import { News } from '../../api/news'
import {
  CREATE_NEWS,
  DELETE_NEWS,
  SET_API_STATUS_ERROR,
  SET_API_STATUS_UNKNOWN_ERROR,
  SET_NEWS
} from '../mutation-types'

const state = () => ({
  news: []
})

const getters = {
  news: state => state.news
}

const mutations = {
  [CREATE_NEWS] (state, news) {
    state.news = [...state.news, news]
  },
  [DELETE_NEWS] (state, id) {
    state.news = state.news.filter(news => {
      return news.id !== id
    })
  },
  [SET_NEWS] (state, { news }) {
    state.news = news
  }
}

const actions = {
  createNews ({ commit }, newsData) {
    News.create(newsData).then(
      response => {
        commit(CREATE_NEWS, response.data)
        router.push({ name: 'news' })
      },
      error => {
        if (error.response.status === 400) {
          commit(SET_API_STATUS_ERROR, error.response.data)
        } else {
          commit(SET_API_STATUS_UNKNOWN_ERROR)
        }
      }
    )
  },
  deleteNews ({commit}, news) {
    News.delete(news).then(
      response => {
        commit(DELETE_NEWS, news)
      },
      error => {
        if (error.response.status === 400) {
          commit(SET_API_STATUS_ERROR, error.response.data['message'])
        } else {
          commit(SET_API_STATUS_UNKNOWN_ERROR)
        }
      })
  },
  getNews ({ commit }) {
    News.list().then(news => {
      commit(SET_NEWS, { news })
    })
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
