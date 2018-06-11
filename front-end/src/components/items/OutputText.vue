<template>
    <module-item v-bind:title="title">
        <span>{{value}}</span>
    </module-item>
</template>



<script>
import ModuleItem from "./ModuleItem.vue";

export default {
  props: ["title", "value"],
  components: {
    ModuleItem
  },
  data() {
    return {
      //   value: "some value"
    };
  }
};
</script>



<style scoped>
</style>
