import { mainAPI, securedAPI } from './common'

export const News = {
  create (newsData) {
    return new Promise((resolve, reject) => {
      securedAPI
        .post('/news/news/', newsData)
        .then(response => {
          resolve(response)
        }, error => {
          reject(error)
        })
    })
  },
  delete (id) {
    return new Promise((resolve, reject) => {
      mainAPI
        .delete(`/news/news/${id}/`)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  list () {
    return mainAPI.get(`/news/news/`).then(response => {
      return response.data
    })
  }
}
