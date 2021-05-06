<template>
<div>
  <h1>Экзаменационный билет {{ examcarddetail.number }}</h1>

  <!-- Список вопросов -->
  <div class="question-list">
    <div
      class="bg-gray question"
      v-for="(question, index) in examcarddetail.questions"
      :key="index"
    >
      <p>
        <strong>
          {{ question.title }}
        </strong>
        <input
          type="button"
          class="btn btn-link"
          value="Удалить"
          @click="deleteQuestion(question.id)"
        >
      </p>
      <p>
        {{ question.content }}
      </p>
      <form v-if="question.answer_type=='TA'" class="form-group">
        <input type="text" class="form-input">
      </form>
      <form v-if="question.answer_type=='SC'" class="form-group">
        <label
          class="form-radio form-inline"
          v-for="(label, index) in question.labels"
          :key="index"
        >
          <input
            type="radio"
            name="label"
            value="index"
          ><i class="form-icon"></i>{{ label.label }}
        </label>
      </form>
      <form v-if="question.answer_type=='MC'" class="form-group">
        <label
          class="form-checkbox form-inline"
          v-for="(label, index) in question.labels"
          :key="index"
        >
          <input
            type="checkbox"
            name="label"
            value="index"
          ><i class="form-icon"></i>{{ label.label }}
        </label>
      </form>
      <form
        v-if="question.answer_type=='SF'"
        class="form-group"
      >
        <input
          class="form-input"
          type="file"
        >
      </form>
    </div>
  </div>

  <create-question></create-question>
</div>
</template>

<script>
import { mapGetters } from 'vuex'
import CreateQuestion from './CreateQuestion'

export default ({
  name: 'examcardDetail',
  methods: {
    deleteQuestion (id) {
      this.$store.dispatch('deleteQuestion', id)
    }
  },
  computed: mapGetters(['examcarddetail']),
  beforeMount () {
    this.$store.dispatch('getExamcarddetail', this.$route.params.id)
  },
  components: {
    'create-question': CreateQuestion
  }
})
</script>

<style>
.question {
  border-radius: 5px;
  margin: 5px 0;
  max-width: 800px;
  min-width: 300px;
  padding: 10px;
}
</style>
