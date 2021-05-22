import { mainAPI, securedAPI } from './common'

export const Exam = {
  create (theme) {
    return new Promise((resolve, reject) => {
      securedAPI
        .post('/exams/exams/', theme)
        .then(response => {
          resolve(response)
        }, error => {
          reject(error)
        })
    })
  },
  delete (exam) {
    return new Promise((resolve, reject) => {
      securedAPI
        .delete(`/exams/exams/${exam.id}/`)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  detail (exam) {
    return mainAPI.get(`/exams/exams/${exam}/detail/`).then(response => {
      return response.data
    })
  },
  list () {
    return mainAPI.get('/exams/exams/').then(response => {
      return response.data
    })
  },
  update (exam, theme) {
    return securedAPI.put(`/exams/exams/${exam}/`, theme).then(response => {
      return response.data
    })
  }
}
