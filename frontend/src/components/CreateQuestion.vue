<template>
  <div class="add-question bg-gray">

    <!-- Добавление нового вопроса -->
    <h3>Добавить вопрос</h3>
    <form class="form-group" @submit="addQuestion">
      <input
        class="form-input"
        type="text"
        v-model="content"
        placeholder="Содержание вопроса"
        required
      >
      <span>В каком виде принимается ответ:</span>
      <select class="form-select" v-model="selectedAnswerType">
        <option
          v-for="(answerType, index) in answerTypes"
          :value="answerType.value"
          :key="index"
        >
        {{ answerType.text }}
        </option>
      </select>
      <button class="btn btn-primary" v-if="isValidated">
        Добавить вопрос
      </button>
    </form>

    <!--  Добавление вариантов ответа  -->
    <div v-if="isAddLabelMode">
      <p
        v-for="(label, index) in labels"
        :key="index"
      >
        {{ label.text }}
      </p>
      <form
        class="form-group input-group"
        @submit="addLabel"
      >
        <input
          class="form-input"
          type="text"
          v-model="label_text"
        >
        <label class="form-checkbox form-inline">
          <input
            type="checkbox"
            name="label"
            v-model="label_is_correct"
          ><i class="form-icon"></i>Верный вариант
        </label>
        <button class="btn btn-primary">
          Добавить вариант ответа
        </button>
      </form>
    </div>

  </div>
</template>

<script>
export default ({
  name: 'create-question',
  data () {
    return {
      isAddLabelMode: false,
      isValidated: true,
      label_text: '',
      label_is_correct: false,
      labels: [],
      content: '',
      selectedAnswerType: 'TA',
      answerTypes: [
        { text: 'Текстовый ответ', value: 'TA' },
        { text: 'Выбор единственного варианта', value: 'SC' },
        { text: 'Выбор нескольких вариантов', value: 'MC' },
        { text: 'Загрузка файла', value: 'SF' }
      ]
    }
  },
  methods: {
    addQuestion (event) {
      this.createQuestion()
      this.content = ''
      this.labels = []
      this.selectedAnswerType = 'TA'
      event.preventDefault()
    },
    createQuestion () {
      this.$store.dispatch('createQuestion', {
        examcard: this.$route.params.id,
        content: this.content,
        answer_type: this.selectedAnswerType,
        labels: this.labels
      })
    },
    addLabel (event) {
      this.labels.push({
        'text': this.label_text,
        'is_correct': this.label_is_correct
      })
      this.label_text = ''
      this.label_is_correct = false
      event.preventDefault()
    }
  },
  watch: {
    selectedAnswerType: function changeMode () {
      if (this.selectedAnswerType === 'SC' || this.selectedAnswerType === 'MC') {
        this.isAddLabelMode = true
        this.isValidated = false
      } else {
        this.isAddLabelMode = false
        this.labels = []
      }
    },
    labels: function checkLabels () {
      if (!this.isAddLabelMode || (this.labels.length > 1)) {
        this.isValidated = true
      } else {
        this.isValidated = false
      }
    }
  }
})
</script>

<style>
.add-question {
  border: rgb(87, 85, 217) solid 1px;
  border-radius: 5px;
  margin: 5px 0;
  max-width: 800px;
  min-width: 300px;
  padding: 10px;
}
</style>
