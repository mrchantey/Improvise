<template lang="pug">
    PageItem(title="Typed Command")
        Label(v-bind:text="command")
</template>




<script lang="ts">
import PageItem from "../../components/PageItem.vue";
import Label from "../../components/Label.vue";
import CommandOptions from "../../js/CommandOptions.js";

import Vue from "vue";
export default Vue.extend({
  data() {
    return {
      command: CommandOptions.GetDefaultCommand()
    };
  },
  components: {
    PageItem,
    Label
  }
});
</script>
