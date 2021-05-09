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
      <!-- Текст вопроса -->
      <p>
        {{ question.content }}
      </p>
      <!-- Текстовый ответ -->
      <form v-if="question.answer_type=='TA'" class="form-group">
        <input type="text" class="form-input" disabled>
      </form>
      <!-- Один правильный вариант ответа -->
      <form v-else-if="question.answer_type=='SC'" class="form-group">
        <label-list
          :labels="question.labels"
          :is_many="false"
        ></label-list>
      </form>
      <!-- Несколько правильных вариантов -->
      <form v-else-if="question.answer_type=='MC'" class="form-group">
        <label-list
          :labels="question.labels"
          :is_many="true"
        ></label-list>
      </form>
      <!-- Ответ в виде файла -->
      <form
        v-else-if="question.answer_type=='SF'"
        class="form-group"
      >
        <input
          class="form-input"
          type="file"
          disabled
        >
      </form>
      <!-- Удаление вопроса -->
      <p>
        <input
          type="button"
          class="btn btn-link"
          value="Удалить"
          @click="deleteQuestion(question.id)"
        >
      </p>

    </div>
  </div>

  <create-question></create-question>
</div>
</template>

<script>
import { mapGetters } from 'vuex'
import CreateQuestion from './CreateQuestion'
import LabelList from './LabelList'

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
    'create-question': CreateQuestion,
    'label-list': LabelList
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
