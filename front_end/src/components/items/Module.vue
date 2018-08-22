<template>

<div class="container">
  <div class="content">
    <div class="title">{{title}}</div>
    <hr>
    <slot></slot>
  </div>
</div>

</template>


<script>
export default {
  props: ["title"]
};
</script>


<style scoped>
.container {
  display: grid;
  grid-template-columns: 1fr minmax(5em, 50em) 1fr;
  /* grid-template-columns: 1fr minmax() 1fr; */
}

.content {
  background-color: #ffffff;
  grid-column-start: 2;
  grid-column-end: 3;
  padding: 1em;
}

.title {
  font-size: 2em;
  text-align: center;
}
</style>