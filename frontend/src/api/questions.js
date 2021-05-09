import { HTTP } from './common'

export const Question = {
  create (questionData) {
    return new Promise((resolve, reject) => {
      HTTP
        .post('/exams/questions/', questionData)
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
        .delete(`/exams/questions/${id}/`)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}
