<template>
    <div>
            <table-actions 
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
      robot: window.$apiInterface.robot
    };
  }
};
</script>
