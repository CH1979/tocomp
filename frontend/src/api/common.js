import axios from 'axios'
import store from '../store'

const APIUrl = 'https://toc.com:8000/api/v1/'

const mainAPI = axios.create({
  baseURL: APIUrl,
  withCredentials: true
})

const securedAPI = axios.create({
  baseURL: APIUrl,
  withCredentials: true
})

securedAPI.interceptors.request.use(function (config) {
  let currentDate = new Date()
  if (currentDate < store.getters.access_token_expiration) {
    store.dispatch('refreshToken')
  }
  return config
})

export { mainAPI, securedAPI }
