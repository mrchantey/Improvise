<template>
    <div>
        <div class='title'>{{title}}</div>
        <slot></slot>
    </div>

</template>

<script>
export default {
  props: ["title"]
};
</script>

<style scoped>
.title {
  font-size: 1.2em;
  /* display: inline; */
}
</style>
