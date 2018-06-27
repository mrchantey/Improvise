<template>
    <div>
      <module-table 
      v-bind:title="'Connected Robots'">
      <tr>
        <th>Name</th>
        <th>IP Address</th>
        <!-- <th>Connection Status</th> -->
        <th>Behavior State</th>
      </tr>
      <tr>
          <td>{{robotProps.name}}</td>
          <td>{{robotProps.ipAddress}}</td>
          <!-- <td>{{robotProps.isConnected}}</td> -->
          <td>{{robotProps.autoState}}</td>
      </tr>
      </module-table>
      
    </div>

</template>


<script>
import ModuleTable from "../items/ModuleTable.vue";
export default {
  props: ["robotProps"],
  components: {
    ModuleTable
  }
};
</script>



