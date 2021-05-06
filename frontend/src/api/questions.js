import { HTTP } from './common'

export const Question = {
  create (questionData) {
    return new Promise((resolve, reject) => {
      HTTP
        .post('/questions/', questionData)
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
        .delete(`/questions/${id}/`)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}
