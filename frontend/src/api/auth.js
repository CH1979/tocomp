import { mainAPI, securedAPI } from './common'

const User = {
  login (credentials) {
    return new Promise((resolve, reject) => {
      mainAPI({
        method: 'post',
        url: '/auth/login/',
        data: credentials
      })
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  logout () {
    return new Promise((resolve, reject) => {
      mainAPI({
        method: 'post',
        url: '/auth/logout/'
      })
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  info () {
    return new Promise((resolve, reject) => {
      securedAPI({
        method: 'get',
        url: '/auth/user/'
      })
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}

const Token = {
  refresh () {
    return new Promise((resolve, reject) => {
      mainAPI({
        method: 'post',
        url: '/auth/token/refresh/'
      })
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}

export { Token, User }
