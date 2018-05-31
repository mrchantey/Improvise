<template>

<div>
  <div
  v-for="(tag,index) in tags"
  v-bind:key="index"
  >{{tag.name}}
  {{tag.checked}}
    <input type="checkbox" v-model="tag.checked">
  </div>
  <module-list 
  v-bind:title="robot.name + ' Actions'">
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Tags</th>
    </tr>
    <tr v-for="(action,index) in robot.actions"
      v-bind:key="index"
      v-if="tagFilter(action.tags)"
      >
      <td>{{action.name}}</td>
      <td>{{action.type}}</td>
      <td>{{action.tags}}</td>
    </tr>
  </module-list>
</div>





</template>



<script>
import ModuleList from "../items/ModuleList.vue";

export default {
  props: ["robot"],
  components: {
    ModuleList
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
      return actionTags.some(at => validTags.some(vt => at === vt));
    }
  }
};
</script>


<style scoped>
</style>
