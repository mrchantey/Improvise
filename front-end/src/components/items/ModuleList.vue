<template>
<div>
    <module-item v-bind:title="title">
      <table>
        <slot>
          </slot>
      </table>
    </module-item>
</div>

</template>



<script>
import ModuleItem from "./ModuleItem.vue";

export default {
  props: ["title", "headers", "contents"],
  components: {
    ModuleItem
  }
};
</script>

<style>
table {
  width: 100%;
}

th {
  padding: 0.3em;
}
th:nth-child(even) {
  background-color: #eeeeee;
}
th:nth-child(odd) {
  background-color: #eeeeee;
}

tr:nth-child(odd) {
  background-color: #eeeeee;
}
</style>

