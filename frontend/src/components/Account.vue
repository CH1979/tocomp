<template>
  <div>
    <div v-if="user">
      {{ user.username }}
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters(['user'])
  }
}
</script>
