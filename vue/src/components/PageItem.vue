<template lang="pug">
    div
      div(class="title") {{title}}
      slot
</template>


<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  props: {
    title: String
  }
});
</script>

<style scoped>
.title {
  font-size: 1.2em;
}
</style>
