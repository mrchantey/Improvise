<template>
    <module-item v-bind:title="title">
        <div class="functional">
                <span>{{value}}</span>
                <button @click="onDown">-</button>
                <button @click="onUp">+</button>
        </div>
    </module-item>
</template>


<script>
import ModuleItem from "./ModuleItem.vue";

export default {
  props: ["title", "onDown", "onUp", "value"],
  components: {
    ModuleItem
  }
  // data() {
  //   return {
  //     value: -1
  //   };
  // }
};
</script>


<style scoped>
.functional {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
.functional > span {
  text-align: center;
}
</style>
