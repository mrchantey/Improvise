<template>
  <module v-bind:title="'Subtitles'">
<input-checkbox
v-bind:title="'Autoscroll'"
v-bind:onChange="onAutoscrollChange"
v-bind:initialValue="true">
</input-checkbox>
    <div class="contents">
      <div 
      class="phrase"
      v-for="(phrase,index) in speechLog"
      v-bind:key="index">
      {{phrase}}
      </div>
    </div>
  </module>


</template>


<script>
import InputCheckbox from "../items/InputCheckbox.vue";
import Module from "../items/Module.vue";

export default {
  components: {
    InputCheckbox,
    Module
  },
  data() {
    return {
      speechLog: window.$apiInterface.robot.speechLog,
      autoScroll: true
    };
  },
  methods: {
    onAutoscrollChange(val) {
      this.autoScroll = val;
    }
  },
  updated() {
    if (this.autoScroll)
      window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
  }
};
</script>

<style scoped>
.phrase {
  padding: 0.5em;
  margin: 0.5em;
  background-color: #eeeeee;
}
</style>
