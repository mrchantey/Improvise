<template>
<div>
    <module v-bind:title="'Connections'">
      <module-item v-bind:title="'Create a new Connection'">
        <p>Enter IP Address:</p>
        <input v-model="ipAddress" @keypress="onIpKeypress">
        <button @click="onIpSubmit">Submit</button>


      </module-item></module>
</div>

</template>

<script>
import Module from "./items/Module.vue";
import ModuleItem from "./items/ModuleItem.vue";
// import ServerInterface from "./serverInterface.js";
// const serverInterface = ServerInterface();

export default {
  components: {
    Module,
    ModuleItem
  },
  data() {
    return {
      ipAddress: ""
    };
  },
  methods: {
    onIpSubmit() {
      console.log("ip submitted");
      window.$serverInterface.ConnectRobot(this.ipAddress);
    },
    onIpKeypress(event) {
      if (event.key == "Enter") this.onIpSubmit();
    }
  },
  created() {}
};
</script>
