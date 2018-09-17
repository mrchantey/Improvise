<template lang="pug">
    PageItem
        p {{text}}


</template>


<script lang="ts">
import Vue from "vue";
import PageItem from "./PageItem.vue";

export default Vue.extend({
  props: {
    text: String
  },
  components: {
    PageItem
  }
});
</script>
