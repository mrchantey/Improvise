<template>
    <module-item v-bind:title="title">
        <div>{{value}}</div>
    </module-item>
</template>


<script>
import ModuleItem from "./ModuleItem.vue";

export default {
  props: ["title", "value"],
  components: {
    ModuleItem
  }
};
</script>
