<template lang="pug">
  div.listcontainer
    button.collapse(@click="isCollapsed=!isCollapsed") {{isCollapsed ? ">" : "\\/"}}
    p.name {{field.name}}
    button.add(@click="AddField") Add
    div.list(v-if="isCollapsed === false")
      div(v-for="(childCommand,index) in field.value" 
        v-bind:key="index") 
        button.delete(@click="DeleteField(childCommand)") Delete
        typedcommand(
          v-bind:command="childCommand" 
          v-bind:depth="depth + 1")
          //- p Hello world
</template>



<script lang="ts">
import Vue from 'vue'
import TypedCommand from './TypedCommand.vue';
import CommandUtility from "../../js/CommandUtility.js"

export default Vue.extend({
  name:"CommandListField",
  props:{
    field:Object,
    depth:Number
  },
  data(){
    return{
      isCollapsed:true
    }
  },methods:{
    DeleteField(field){
      const arr = this.field.value
      const index = arr.indexOf(field)
      if(index > -1)
        arr.splice(index,1);
    },
    AddField(){
      const defaultCommand = CommandUtility.GetDefaultCommand()
      this.field.value.push(defaultCommand)
    }
  },
  components:{
    TypedCommand
  }
})
</script>


<style scoped>
.listcontainer{
  display:grid;
  grid-template-columns:5em 1fr 10em;
}

.collapse{
  grid-column:1 / 2;
  margin: 1em;
}

.name{
  grid-column:2 / 3;
}

.add{
  grid-column:3 / 4;
  margin: 1em;
}

.list{
  grid-column:1 / 4;
}

</style>