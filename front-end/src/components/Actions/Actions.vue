<template>
    <div>
            <list-actions 
            v-for="(robot,index) in connectedRobots"
            v-bind:key="index"
            v-bind:robot="robot"
            ></list-actions>
    </div>
</template>


<script>
// import Module from "../items/Module.vue";
// import ModuleItem from "../Items/ModuleItem.vue";
import ListActions from "./ListActions.vue";

export default {
  components: {
    // Module,
    // ModuleItem,
    ListActions
  },
  data() {
    return {
      connectedRobots: window.$serverInterface.connectedRobots
    };
  }
};
</script>
