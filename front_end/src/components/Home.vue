<template>
<div>
  <module v-bind:title="'Home'">
    <module-item v-bind:title="'Welcome'">
    <p>This is the Improvise app for the Mark Moran Group.</p>
    <p>It is intended to provide a platform for staff to operate the NAO Robots.</p>
    <p>To Get Started, jump to the 'Connection' Tab to ensure everything is connected properly.</p>
    
    <p>If you require any assistance please email Peter at phayman@markmoran.com.au</p>
    </module-item>
  </module>
    <!-- <input v-model="naoIP" @keydown="ipKeyDown"> -->
    <!-- <button @click="submit">Submit</button> -->
</div>
</template>

<script>
import Module from "./items/Module.vue";
import ModuleItem from "./items/ModuleItem.vue";
export default {
  components: {
    Module,
    ModuleItem
  },
  data() {
    return {
      naoIP: ""
    };
  },
  methods: {
    submit() {
      this.$router.push("/socket/" + this.naoIP);
      this.naoIP = "";
    },
    ipKeyDown(event) {
      if (event.key === "Enter") this.submit();
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
