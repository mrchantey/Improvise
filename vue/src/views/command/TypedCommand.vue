<template lang="pug">
  div.container
    div.field(v-for="(field,index) in command.fields"
      v-bind:key="index")
      CommandListField.subcommands(
        v-if="field.name === 'commands'"
        v-bind:field="field"
        v-bind:depth="depth"
        )
      GenericField.generic(
        v-else-if=("command.name !== 'name'")
        v-bind:key="index"
        v-bind:field="field"
        v-bind:parentCommand="command"
        )      
</template>


<script lang="ts">
import CommandUtility from "../../js/CommandUtility.js";
import CommandListField from "./CommandListField.vue";
import GenericField from "./GenericField.vue";

import Vue from "vue";
export default Vue.component("typedcommand",{
  components: {
    CommandListField,
    GenericField
  },
  props: {
    command: Object,
    depth: Number
  },
  created() {
    CommandUtility.FilterCommand(this.command);
  },
  methods: {
    AddCommand() {},
    DeleteCommand(command) {}
  }
});
</script>

<style scoped>
.container {
  display:grid;
  grid-template-columns: auto;
  /* border-left-style: solid; */
  /* border-top-style: solid; */
  border-color: gray;
  border-style: solid;
  box-shadow: 0.2em 0.2em 0.5em;
  margin: 1em;
  /* height: 10em; */
}

.field {
  grid-column: 1 / 2;
  /* margin: 0.5em; */
  /* height: 2em; */
  align-self: center;
}

.field:nth-child(even) {
  background-color: lightgray;
}

.field:nth-child(odd) {
  background-color: white;
}

input[type="checkbox"] {
  transform: scale(1.5);
}
</style>
