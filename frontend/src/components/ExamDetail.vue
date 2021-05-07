<template>
  <div id="app">

    <h1>{{ examdetail.theme }}</h1>

    <div class="accordion">
      <div
        v-for="(examcard, index) in examdetail.examcards"
        :key="index"
      >
        <input
          type="radio"
          :id="'accordion-' + index" name="accordion-radio"
          hidden
        >
        <label
          class="accordion-header"
          :for="'accordion-' + index"
        >
          <i class="icon icon-arrow-right mr-1"></i>
          Билет № {{ examcard.number }}
        </label>
        <div class="accordion-body">
          <ul>
            <li v-for="question in examcard.questions" :key="question.id">
              {{ question.title }}
            </li>
          </ul>
        </div>
        <router-link :to="'/examcards/' + examcard.id + '/detail'">
          редактировать
        </router-link>
        <a class="delete-link" @click="deleteExamcard(examcard.id)">удалить</a>
      </div>
    </div>

    <form class="form-group form-inline">
      <input
        type="number"
        placeholder="Номер билета"
        v-model="number"
        required
      >
      <a
        class="btn btn-primary"
        @click="createExamcard()">
        Добавить билет
      </a>
    </form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      number: ''
    }
  },
  name: 'examdetail',
  computed: mapGetters(['examdetail']),
  beforeMount () {
    this.$store.dispatch('getExamdetail', this.$route.params.id)
  },
  methods: {
    createExamcard () {
      let examcardData = {
        'exam': this.$route.params.id,
        'number': this.number
      }
      this.$store.dispatch('createExamcard', examcardData)
    },
    deleteExamcard (id) {
      this.$store.dispatch('deleteExamcard', id)
    }
  }
}
</script>

<style>
.delete-link {
  cursor: pointer;
}
</style>
