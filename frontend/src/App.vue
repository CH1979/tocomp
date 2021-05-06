<template>
  <div id="app" class="container">
    <div class="columns p-2">
      <div class="column col-12">
        <header class="navbar">
          <section class="navbar-section">
            <router-link to="/" class="btn btn-link">
              Главная
            </router-link>
            <router-link to="/exams" class="btn btn-link">
              Список экзаменов
            </router-link>
          </section>
        </header>
      </div>
      <div class="column col-12">
        <router-view></router-view>
      </div>
      <div class="toast toast-error" v-if="apiError"> {{ errorMessage }} </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { SET_API_STATUS_DEFAULT } from './store/mutation-types'

export default {
  computed: {
    ...mapState({
      apiError: state => state.apiError,
      errorMessage: state => state.errorMessage
    })
  },
  watch: {
    apiError () {
      setTimeout(() => {
        this.$store.commit(SET_API_STATUS_DEFAULT)
      }, 2000)
    }
  }
}
</script>

<style>
body {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
div#app {
  width: 90%;
}
</style>
