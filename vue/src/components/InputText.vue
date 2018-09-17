<template lang="pug">
    PageItem(v-bind:title="title")
      textarea(v-model="value" tabindex="1")
      div
      button(@click="onSubmit") Submit
</template>


<script lang="ts">
import Vue from "vue";
import PageItem from "./PageItem.vue";

export default Vue.extend({
  props: {
    title: String,
    submitCallback: Function
  },
  data() {
    return {
      value: `{"commandName":"say","phrase":"hi there"}`
    };
  },
  components: {
    PageItem
  },
  methods: {
    onSubmit() {
      this.submitCallback(this.value);
    }
  }
});
</script>
