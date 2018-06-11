<template>
    <div>
      <module-table 
      v-bind:title="'Connected Robots'">
      <tr>
        <th>Name</th>
        <th>IP Address</th>
        <th>Connection Status</th>
        <th>Behavior State</th>
      </tr>
      <tr v-if="robot.isConnected === true">
          <td>{{robot.name}}</td>
          <td>{{robot.ipAddress}}</td>
          <td>{{robot.isConnected}}</td>
          <td>{{robot.autoState}}</td>
      </tr>
      </module-table>
      
    </div>

</template>


<script>
import ModuleTable from "../items/ModuleTable.vue";
export default {
  props: ["robot"],
  components: {
    ModuleTable
  }
};
</script>



