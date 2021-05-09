<template>
<div>
  <label
  :class="is_many ? 'form-inline form-checkbox' : 'form-inline form-radio'"
  v-for="(label, index) in labels"
  :key="index"
  >
  <input
    :type="is_many ? 'checkbox' : 'radio'"
    name="label"
    value="index"
    v-model="label.is_correct"
  >
  <i class="form-icon"></i>
  {{ label.text }}
  </label>
  <i class="form-icon icon icon-check"></i>
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
