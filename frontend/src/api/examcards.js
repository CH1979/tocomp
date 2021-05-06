import { HTTP } from './common'

export const Examcard = {
  create (examcardData) {
    return new Promise((resolve, reject) => {
      HTTP
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
      HTTP
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
    return HTTP.get(`/examcards/${id}/detail/`).then(response => {
      return response.data
    })
  }
}
