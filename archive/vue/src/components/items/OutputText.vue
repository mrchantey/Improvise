<template>
    <module-item v-bind:title="title">
        <p>{{value}}</p>
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
