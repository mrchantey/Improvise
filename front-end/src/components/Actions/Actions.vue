<template>
    <div>
            <table-actions 
            v-for="(robot,index) in connectedRobots"
            v-bind:key="index"
            v-bind:robot="robot"
            ></table-actions>
    </div>
</template>


<script>
// import Module from "../items/Module.vue";
// import ModuleItem from "../Items/ModuleItem.vue";
import TableActions from "./TableActions.vue";

export default {
  components: {
    // Module,
    // ModuleItem,
    TableActions
  },
  data() {
    return {
      connectedRobots: window.$serverInterface.connectedRobots
    };
  }
};
</script>
