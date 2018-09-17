<template lang="pug">
    PageContent(title="Command")
      Label(text="Welcome to the command tab. Please select a command.")
      RawCommand
      TypedCommand
</template>







<script lang="ts">
import Label from "../../components/Label.vue";
import PageContent from "../../components/PageContent.vue";
import RawCommand from "./RawCommand.vue";
import TypedCommand from "./TypedCommand.vue";
import Vue from "vue";

export default Vue.extend({
  components: {
    Label,
    PageContent,
    RawCommand,
    TypedCommand
  }
});
</script>
