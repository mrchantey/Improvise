<template>
<div>
    <module v-bind:title="'Connections'">
      <module-item v-bind:title="'Create a new Connection'">
        <p>Enter IP Address:</p>
        <input v-model="serverIp" @keypress="onIpKeypress">
        <button @click="onIpSubmit">Submit</button>
      </module-item>
      <list-robots></list-robots>
      </module>
</div>

</template>

<script>
import Module from "../items/Module.vue";
import ModuleItem from "../items/ModuleItem.vue";
import ListRobots from "./ListRobots.vue";

export default {
  components: {
    Module,
    ModuleItem,
    ListRobots
  },
  data() {
    return {
      serverIp: ""
    };
  },
  methods: {
    onIpSubmit() {
      console.log("ip submitted");
      window.$serverInterface.ConnectRobot(this.serverIp);
    },
    onIpKeypress(event) {
      if (event.key == "Enter") this.onIpSubmit();
    }
  },
  created() {}
};
</script>
