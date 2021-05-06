import { HTTP } from './common'

export const Exam = {
  create (theme) {
    return new Promise((resolve, reject) => {
      HTTP
        .post('/exams/', theme)
        .then(response => {
          resolve(response)
        }, error => {
          reject(error)
        })
    })
  },
  delete (exam) {
    return new Promise((resolve, reject) => {
      HTTP
        .delete(`/exams/${exam.id}/`)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  detail (exam) {
    return HTTP.get(`/exams/${exam}/detail/`).then(response => {
      return response.data
    })
  },
  list () {
    return HTTP.get('/exams/').then(response => {
      return response.data
    })
  },
  update (exam, theme) {
    return HTTP.put(`/exams/${exam}/`, theme).then(response => {
      return response.data
    })
  }
}
