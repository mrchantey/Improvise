<template>
    <module-item v-bind:title="title">
        <input type="checkbox" v-model="isChecked" v-on:change="onChange(isChecked)">
    </module-item>


</template>


<script>
import ModuleItem from "./ModuleItem.vue";

export default {
  props: ["title", "onChange", "initialValue"],
  components: {
    ModuleItem
  },
  data() {
    return {
      isChecked: false
    };
  },
  created() {
    if (this.initialValue !== undefined) this.isChecked = this.initialValue;
  }
};
</script>
