<template>
    <module-item v-bind:title="title">
        <input @keypress="onTextboxKeyPress" v-model="value" tabindex="1">
        <button @click="onEnter">Submit</button>
        <slot></slot>
    </module-item>    
</template>


<script>
// import ModuleItem from "./ModuleItem.vue";
import ModuleItem from "./ModuleItem.vue";

export default {
  props: ["title", "onEnterCallback"],
  components: {
    ModuleItem
  },
  data() {
    return {
      value: ""
    };
  },
  methods: {
    onEnter() {
      this.onEnterCallback(this.value);
      this.value = "";
    },
    onTextboxKeyPress(event) {
      if (event.key == "Enter") this.onEnter();
    }
  }
};
</script>
