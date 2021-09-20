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
      <input
        type="file"
        id="image"
        ref="image"
        accept="image/*"
        @change="onFileChange"
      >
      <img
        class="img-responsive"
        v-bind="imagePreview"
        v-show="showPreview"
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
import { mapGetters } from 'vuex'

export default ({
  name: 'create-news',
  data () {
    return {
      title: '',
      content: '',
      image: '',
      showPreview: false,
      imagePreview: ''
    }
  },
  methods: {
    addNews (event) {
      let formData = new FormData()
      formData.append('image', this.image)
      formData.append('title', this.title)
      formData.append('content', this.content)
      formData.append('author', this.user)
      console.log(formData)
      this.$store.dispatch('createNews', formData)
      event.preventDefault()
    },
    onFileChange () {
      this.image = this.$refs.image.files[0]

      let reader = new FileReader()

      reader.addEventListener('load', function () {
        console.log(this.showPreview)
        console.log(this.imagePreview)
      }.bind(this), false)

      if (this.file) {
        if (/\.(jpe?g|png|gif)$/i.test(this.file.name)) {
          reader.readAsDataURL(this.file)
        }
      }
    },
    removeImage () {}
  },
  computed: {
    ...mapGetters(['user'])
  }

})
</script>
