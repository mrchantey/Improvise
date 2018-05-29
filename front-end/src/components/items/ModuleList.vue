<template>
<div>
    <module-item v-bind:title="title">
        <slot>
        </slot>
    </module-item>
</div>

</template>



<script>
import ModuleItem from "./ModuleItem.vue";

export default {
  props: ["title"],
  components: {
    ModuleItem
  }
};
</script>
