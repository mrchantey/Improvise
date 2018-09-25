<template lang="pug">
  div
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
import Vue from "vue";
import CommandUtility from "../../js/CommandUtility.js"

export default Vue.extend({
  props: {
    parentCommand:Object,
    field: Object
  },
  methods:{
      OnFieldUpdate() {
      CommandUtility.FilterCommand(this.parentCommand);
    }
  }
});
</script>


<style scoped>

div {
  display: grid;
  max-width: 30em;
  grid-template-columns: 1fr 1fr;
}
.name {
  /* background-color: aqua; */
  grid-column: 1;
}
.value {
  /* background-color: blueviolet; */
  color: chartreuse;
  font-size: 2em;
  grid-column: 2;
}

</style>