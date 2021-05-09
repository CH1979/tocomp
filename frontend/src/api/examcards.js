import { HTTP } from './common'

export const Examcard = {
  create (examcardData) {
    return new Promise((resolve, reject) => {
      HTTP
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
      HTTP
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
    return HTTP.get(`/exams/examcards/${id}/detail/`).then(response => {
      return response.data
    })
  }
}
