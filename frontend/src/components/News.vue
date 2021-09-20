<template>
  <!--   Новости   -->
  <div class="column col-12">
    <h1>Новости</h1>
    <router-link to="/news/add" v-if="user">Добавить новость</router-link>
    <div
      v-for="news_item in news"
      :key="news_item.id"
    >
      <h2>{{ news_item.title }}</h2>
      <div>
        <p
          v-for="(paragraph, index) in news_item.content.split('\n')"
          :key="index"
        >
          {{ paragraph }}
        </p>
      </div>
      <div>
        <img class="img-responsive" :src="news_item.image">
      </div>
      <div class="columns">
        <div class="column col-6">
          Автор:
          {{ news_item.author.first_name }}
          {{ news_item.author.last_name }}
        </div>
        <div class="column col-6 text-right">
          Опубликовано: {{ news_item.created_at | localeDate }}
        </div>
      </div>
      <input
        class="btn btn-link"
        type="button"
        value="удалить"
        v-if="user"
        @click="deleteNews(news_item.id)"
      />
    </div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  name: 'news-list',
  methods: {
    deleteNews (newsId) {
      this.$store.dispatch('deleteNews', newsId)
    }
  },
  computed: {
    ...mapGetters(['news', 'user'])
  },
  filters: {
    localeDate: function (value) {
      return (new Date(value)).toLocaleString()
    }
  },
  beforeMount () {
    this.$store.dispatch('getNews')
  }
}
</script>

<style>
p {
  margin: 0.2rem 0;
}
</style>
