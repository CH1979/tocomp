import { mainAPI, securedAPI } from './common'

export const Examcard = {
  create (examcardData) {
    return new Promise((resolve, reject) => {
      securedAPI
        .post('/examcards/', examcardData)
        .then(response => {
          resolve(response)
        }, error => {
          reject(error)
        })
    })
  },
  delete (id) {
    return new Promise((resolve, reject) => {
      securedAPI
        .delete(`/examcards/${id}/`)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  list (id) {
    return mainAPI.get(`/examcards/${id}/`).then(response => {
      return response.data
    })
  }
}
