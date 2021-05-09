<template>
<div>
  <span
    class="answer_label bg-secondary"
    v-for="(label, index) in labels"
    :key="index"
  >
  <i
    v-if="label.is_correct"
    class="form-icon icon icon-check">
  </i>
  {{ label.text }}
  </span>
</div>
</template>

<script>
export default {
  name: 'label-list',
  props: {
    labels: Array,
    is_many: Boolean
  }
}
</script>

<style>
.answer_label {
  /*border: gray dotted 1px;*/
  border-radius: 2px;
  display: inline-block;
  margin: 0 2px;
  min-width: 100px;
  padding: 0 5px;
}
</style>
