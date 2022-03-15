<template>
  <div id="app" class="container grid-lg">
    <div class="columns p-2">
      <div class="column col-12">
        <header class="navbar">
          <section class="navbar-section">
            <router-link to="/" class="btn btn-link">
              Главная
            </router-link>
            <router-link to="/news" class="btn btn-link">
              Новости
            </router-link>
            <router-link to="/exams" class="btn btn-link">
              Список экзаменов
            </router-link>
          </section>
          <section class="navbar-section">
            <router-link to="/account" class="btn btn-secondary" v-if="user">
              Личный кабинет
            </router-link>
            <router-link to='/login' class="btn btn-primary" v-if="!user">
              Войти
            </router-link>
            <router-link to='/logout' class="btn btn-primary" v-if="user">
              Выйти
            </router-link>
          </section>
        </header>
      </div>
      <div class="column col-12">
        <router-view></router-view>
      </div>
      <transition name="fade">
        <div class="toast toast-error error-message" v-if="apiError">
          {{ errorMessage }}
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { SET_API_STATUS_DEFAULT } from './store/mutation-types'

export default {
  computed: {
    ...mapGetters([
      'apiError',
      'errorMessage',
      'user'
    ])
  },
  watch: {
    apiError () {
      setTimeout(() => {
        this.$store.commit(SET_API_STATUS_DEFAULT)
      }, 1500)
    }
  },
  beforeMount () {
    this.$store.dispatch('refreshToken')
    this.$store.dispatch('userCheck')
  }
}
</script>

<style>
body {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: #eee;
}
.container {
  background-color: #fff;
}
.error-message {
  border-radius: 5px;
  position: fixed;
  top: 50px;
  left: 50%;
  width: 400px;
  margin-left: -200px; /* Половина ширины */
}
.fade-enter-active, .fade-leave-active {
  transition: opacity 500ms;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
