<template>
    <div>
      <module-list v-bind:title="'Connected Robots'">
        <div class="row headings">
          <div class="name">Name</div>
          <div class="ip">IP Address</div>
          <div class="id">Session Id</div>
          <div class="status">Status</div>
        </div>
        <connected-robot class="row content"
          v-for="(robot,index) in connectedRobots"
          v-bind:key="index"
          v-bind:robot="robot"
        ></connected-robot>
      </module-list>
    </div>

</template>


<script>
import ModuleList from "./ModuleList.vue";
import ConnectedRobot from "./ConnectedRobot.vue";
export default {
  components: {
    ModuleList,
    ConnectedRobot
  },
  data() {
    return {
      connectedRobots: window.$serverInterface.connectedRobots
    };
  }
};
</script>


<style scoped>
.list {
  background-color: aquamarine;
}

.row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  padding: 0.3em;
}

.headings {
  background-color: #cccccc;
  font-size: 1.2em;
}
</style>
