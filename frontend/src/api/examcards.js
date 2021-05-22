import { mainAPI, securedAPI } from './common'

export const Examcard = {
  create (examcardData) {
    return new Promise((resolve, reject) => {
      securedAPI
        .post('/exams/examcards/', examcardData)
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
        .delete(`/exams/examcards/${id}/`)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  list (id) {
    return mainAPI.get(`/exams/examcards/${id}/detail/`).then(response => {
      return response.data
    })
  }
}
