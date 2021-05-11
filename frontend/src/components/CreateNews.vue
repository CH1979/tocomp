<template>
  <div>
    <h1>Добавить новость</h1>
    <form class="form-group" @submit="addNews">
      <input
        class="form-input"
        v-model="title"
        placeholder="Заголовок"
        required
      >
      <textarea
        class="form-input"
        v-model="content"
        placeholder="Содержание новости"
        rows="5"
      ></textarea>
      <button class="btn btn-primary">
        Добавить новость
      </button>
    </form>
  </div>
</template>

<script>
export default ({
  name: 'create-news',
  data () {
    return {
      title: '',
      content: ''
    }
  },
  methods: {
    addNews (event) {
      this.createNews()
      this.title = ''
      this.content = ''
      event.preventDefault()
    },
    createNews () {
      this.$store.dispatch('createNews', {
        title: this.title,
        content: this.content
      })
    }
  }
})
</script>
