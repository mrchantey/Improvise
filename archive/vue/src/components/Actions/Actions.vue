<template>
    <module v-bind:title="robot.properties.name + ' Actions'"> 
            <table-actions 
            v-bind:robot="robot"
            ></table-actions>
    </module>
</template>


<script>
import Module from "../items/Module.vue";
import TableActions from "./TableActions.vue";

export default {
  components: {
    Module,
    TableActions
  },
  data() {
    return {
      robot: window.$apiInterface.robot
    };
  }
};
</script>
