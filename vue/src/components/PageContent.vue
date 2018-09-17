<template lang="pug">
    div(class="pageContainer")
        div(class="pageContent")
            div(class="title") {{title}}
            hr
            slot
</template>




<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  props: ["title"]
});
</script>



<style scoped>
.pageContainer {
  display: grid;
  grid-template-columns: 1fr minmax(5em, 50em) 1fr;
}
.pageContent {
  background-color: #ffffff;
  grid-column-start: 2;
  grid-column-end: 3;
}
.title {
  font-size: 2em;
}
</style>