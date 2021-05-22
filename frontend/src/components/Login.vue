<template>
<div>
  <form @submit="userSignIn">
    <input type="text" v-model="username">
    <input type="password" v-model="password">
    <button>Войти</button>
  </form>
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
      })
    }
  }
}
</script>
