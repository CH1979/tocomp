<template>
<div>
  <div class="modal modal-sm active" id="modal-id">
    <div class="modal-container">
      <div class="modal-header">
        <router-link to="/" class="btn btn-clear float-right" aria-label="Close"></router-link>
        <div class="modal-title h4">Вход</div>
      </div>
      <div class="modal-body">
        <form @submit="userSignIn">
          <label class="form-label">Имя пользователя</label>
          <input class="form-input" type="text" v-model="username" placeholder="Имя пользователя">
          <label class="form-label">Пароль</label>
          <input class="form-input" type="password" v-model="password" placeholder="Пароль">
          <button class="btn btn-primary">Войти</button>
        </form>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'login-form',
  data: () => {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    userSignIn (event) {
      this.userLogin()
      this.username = ''
      this.password = ''
      event.preventDefault()
    },
    userLogin () {
      this.$store.dispatch('userLogin', {
        username: this.username,
        password: this.password
      }).then(() => this.$router.push({name: 'account'}))
    }
  }
}
</script>
