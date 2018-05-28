<template>
<div>
    <module v-bind:title="'Settings'">Im in the module</module>
</div>

</template>

<script>
import Module from "./items/Module.vue";

export default {
  components: {
    Module
  }
};
</script>
