import { HTTP } from './common'

export const News = {
  create (newsData) {
    return new Promise((resolve, reject) => {
      HTTP
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
      HTTP
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
    return HTTP.get(`/news/news/`).then(response => {
      return response.data
    })
  }
}
