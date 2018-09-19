<template lang="pug">
  div.container
    //- p {{title}}
    div.field(v-for="(field,index) in command.fields" v-bind:key="index")
          span.subcommands(v-if="field.name === 'commands'")
            p.name {{field.name}}
            TypedCommand.value(
              v-for="(childCommand,index) in field.value" 
              v-bind:key="index" 
              v-bind:command="childCommand" 
              v-bind:depth="depth + 1")
          span.generic(v-else)
            p.name {{field.name}}
            span.value
              select(
                v-if="field.options !== undefined" 
                v-model="field.value" 
                @change="OnFieldUpdate")
                option(v-for="(option,index) in field.options" v-bind:key="index")
                  p {{option}}
              span(v-else)
                input(v-if="typeof(field.value) === 'string'" type="text" v-model="field.value" @input="OnFieldUpdate")
                input(v-if="typeof(field.value) === 'number'" type="text" v-model="field.value" @input="OnFieldUpdate")
                input(v-if="typeof(field.value) === 'boolean'" type="checkbox" v-model="field.value")
</template>


<script lang="ts">
import CommandUtility from "../../js/CommandUtility.js";

import Vue from "vue";
export default Vue.extend({
  name: "TypedCommand",
  props: {
    command: Object,
    depth: Number
  },
  created() {
    CommandUtility.FilterCommand(this.command);
    // this.command.fields.forEach(f => console.log(f.name, f.value));
  },
  methods: {
    OnFieldUpdate() {
      // console.log(this.command.fields);
      CommandUtility.FilterCommand(this.command);
    }
  }
});
</script>

<style scoped>
.container {
  /* border-left-style: solid; */
  /* border-top-style: solid; */
  border-color: gray;
  border-style: solid;
  margin: 1em;
  /* height: 10em; */
}

.field {
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

.generic {
  display: grid;
  max-width: 30em;
  grid-template-columns: 1fr 1fr;
}

.generic > .name {
  /* background-color: aqua; */
  grid-column: 1;
}
.generic > .value {
  /* background-color: blueviolet; */
  color: chartreuse;
  font-size: 2em;
  grid-column: 2;
}
input[type="checkbox"] {
  transform: scale(1.5);
}
</style>
