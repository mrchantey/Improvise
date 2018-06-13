<template>

<div>
  <module-table 
  v-bind:title="robot.name + ' Actions'">
  <div
    v-for="(tag,index) in tags"
    v-bind:key="index">
    {{tag.name}}
    {{tag.checked}}
    <input type="checkbox" v-model="tag.checked">
  </div>
    <tr>
      <th>Name</th>
      <th>ID</th>
      <th>Type</th>
      <th>Tags</th>
      <th>Controls</th>
    </tr>
    <tr v-for="(action,index) in robot.actions"
      v-bind:key="index"
      v-if="tagFilter(action.tags)"
      >
      <td>{{action.name}}</td>
      <td>{{action.id}}</td>
      <td>{{action.type}}</td>
      <td>{{action.tags}}</td>
      <td><button @click="()=>RunAction(action.id)">Run</button></td>
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
  },
  data() {
    return {
      tags: [
        { name: "animations", checked: false },
        { name: "Positive", checked: false },
        { name: "Stand", checked: false },
        { name: "Neutral", checked: false }
      ]
    };
  },
  methods: {
    tagFilter(actionTags) {
      const validTags = this.tags
        .filter(t => t.checked === true)
        .map(t => t.name);
      // console.log(actionTags[0]);
      // return true;
      // return actionTags.some(at => validTags.some(vt => at === vt));
      return actionTags;
    },
    RunAction(actionId) {
      this.robot.RunAction(actionId);
    }
  }
};
</script>


<style scoped>
</style>
