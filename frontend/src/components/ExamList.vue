<template>
  <div class="columns">

    <!--   Список экзаменов   -->
    <div class="column col-12">
      <h1>Список экзаменов</h1>
      <table class="table">
        <tbody>
          <tr
            v-for="exam in exams"
            :key="exam.id"
          >
            <td>
              {{ exam.theme }}
            </td>
            <td>
              <router-link
                class="btn btn-link"
                :to="'/exams/' + exam.id + '/detail'">

                редактировать
              </router-link>
              <input
                class="btn btn-link"
                type="button"
                value="удалить"
                @click="deleteExam(exam)"
              />
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!--   Добавление нового экзамена   -->
    <div class="column col-8">
      <form class="form-group" @submit="submitForm">
        <label class="form-label">Тема экзамена</label>
        <input
          class="form-input"
          type="text"
          v-model="theme"
          placeholder="Введите тему экзамена..."
        >
        <button class="btn btn-primary">
          Добавить экзамен
        </button>
      </form>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'exam-list',
  data () {
    return {
      theme: ''
    }
  },
  methods: {
    submitForm (event) {
      this.createExam()
      this.theme = ''
      event.preventDefault()
    },
    createExam () {
      this.$store.dispatch('createExam', { theme: this.theme })
    },
    deleteExam (exam) {
      this.$store.dispatch('deleteExam', exam)
    }
  },
  computed: {
    ...mapGetters(['exams'])
  },
  beforeMount () {
    this.$store.dispatch('getExams')
  }
}
</script>
