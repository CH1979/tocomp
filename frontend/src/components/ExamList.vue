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
    <div class="add-exam bg-gray">
      <form class="form-group" @submit="submitForm">
        <label class="form-label">Добавить экзамен</label>
        <input
          class="form-input"
          type="text"
          v-model="theme"
          placeholder="Введите тему экзамена..."
          required
        >
        <button class="btn btn-primary">
          OK
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

<style>
.add-exam {
  border: rgb(87, 85, 217) solid 1px;
  border-radius: 5px;
  display: block;
  margin: 5px 0;
  max-width: 800px;
  min-width: 300px;
  padding: 10px;
  position: sticky;
  bottom: 0;
}
</style>
