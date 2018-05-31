<template>
    <div>
      <module-list 
      v-bind:title="'Connected Robots'">
      <tr>
        <th>Name</th>
        <th>IP Address</th>
        <th>Session ID</th>
        <th>Status</th>
      </tr>
      <tr v-for="(robot,index) in robots"
        v-bind:key="index">
          <td>{{robot.name}}</td>
          <td>{{robot.ipAddress}}</td>
          <td>{{robot.sessionId}}</td>
          <td>Connected</td>
      </tr>
      </module-list>
      
    </div>

</template>


<script>
import ModuleList from "../items/ModuleList.vue";
export default {
  components: {
    ModuleList
  },
  data() {
    return {
      robots: window.$serverInterface.connectedRobots
    };
  }
};
</script>



