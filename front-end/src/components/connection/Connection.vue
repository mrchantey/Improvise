<template>
<div>
    <module v-bind:title="'Connections'">
      <output-text 
      v-bind:title="'Server Status:'"
      v-bind:value="apiConnected"
      ></output-text>
      
      <!-- <module-item v-bind:title="'Create a new Connection'">
        <p>Enter IP Address:</p>
        <input v-model="serverIp" @keypress="onIpKeypress">
        <button @click="onIpSubmit">Submit</button>
      </module-item> -->
      <table-robots v-bind:robot="robot"></table-robots>
      </module>
</div>

</template>

<script>
import Module from "../items/Module.vue";
import ModuleItem from "../items/ModuleItem.vue";
import TableRobots from "./TableRobots.vue";
import OutputText from "../items/OutputText.vue";

export default {
  components: {
    Module,
    ModuleItem,
    TableRobots,
    OutputText
  },
  data() {
    return {
      serverIp: "",
      apiConnected: window.$apiInterface.connectionStatus,
      robot: window.$apiInterface.robot
    };
  }
  // methods: {
  //   onIpSubmit() {
  //     console.log("ip submitted");
  //     window.$serverInterface.ConnectRobot(this.serverIp);
  //   },
  //   onIpKeypress(event) {
  //     if (event.key == "Enter") this.onIpSubmit();
  //   }
  // },
};
</script>
