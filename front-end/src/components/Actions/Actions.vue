<template>
    <div>
        <module v-bind:title="'Actions'">
            <li-item 
            v-for="(robot,index) in connectedRobots"
            v-bind:key="index"
            v-bind:robot="robot"
            ></module-item>


    </div>
</template>


<script>
import Module from "../items/Module.vue";
import ModuleItem from "./Items/ModuleItem.vue";

export default {
  components: {
    Module,
    ModuleItem
  },
  data() {
    return {
      connectedRobots: window.$serverInterface.connectedRobots
    };
  }
};
</script>
