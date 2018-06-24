<template>
<div v-if="robot!= undefined">
  <module 
  v-bind:title="robot.properties.name+ ' Remote Controller'">
  <div class="contents">
  <input-range
  v-bind:title="'Master Volume'"
  v-bind:onDown="()=>propertyDown('volume')"
  v-bind:onUp="()=>propertyUp('volume')"
  v-bind:value="robot.properties.volume"
  ></input-range>
  <input-range
  v-bind:title="'Speech Volume'"
  v-bind:onDown="()=>propertyDown('speechVolume')"
  v-bind:onUp="()=>propertyUp('speechVolume')"
  v-bind:value="robot.properties.speechVolume"
  ></input-range>
  <input-range
  v-bind:title="'Speech Speed'"
  v-bind:onDown="()=>propertyDown('speechSpeed')"
  v-bind:onUp="()=>propertyUp('speechSpeed')"
  v-bind:value="robot.properties.speechSpeed"
  ></input-range>
  <input-range
  v-bind:title="'Speech Pitch'"
  v-bind:onDown="()=>propertyDown('speechPitch')"
  v-bind:onUp="()=>propertyUp('speechPitch')"
  v-bind:value="robot.properties.speechPitch"
  ></input-range>
  <module-item v-bind:title="'Buttons'">
    <button @click="stopAll" tabindex="2">Stop All</button>
    <button @click="wakeUp" tabindex="3">Wake Up</button>
    <button @click="goToSleep" tabindex="4">Go To Sleep</button>
  </module-item>
  <module-item v-bind:title="'Say A Phrase'">
    <input @keypress="sayPhraseKeyPress" v-model="phraseToSay" tabindex="1">
    <button @click="sayPhrase">Say</button>
      <label>
      <input type="checkbox" v-model="sayAnimated">
      Say Animated
      </label>
  </module-item>
  </div>
  </module>
</div>
</template>


<script>
import Module from "../items/Module.vue";
import ModuleItem from "../items/ModuleItem.vue";
import InputRange from "../items/InputRange.vue";

export default {
  components: {
    Module,
    ModuleItem,
    InputRange
  },
  data() {
    return {
      phraseToSay: "",
      sayAnimated: false,
      robot: window.$apiInterface.robot
    };
  },
  methods: {
    propertyDown(propName) {
      this.robot.SetProperty(propName, this.robot.properties[propName] - 10);
    },
    propertyUp(propName) {
      this.robot.SetProperty(propName, this.robot.properties[propName] + 10);
    },
    wakeUp() {
      this.robot.DoMethod("SetAutoState", ["solitary"]);
    },
    stopAll() {
      this.robot.DoMethod("StopAll");
    },
    goToSleep() {
      this.robot.DoMethod("SetAutoState", ["disabled"]);
    },
    sayPhrase() {
      this.robot.DoMethod("Say", [this.phraseToSay, this.sayAnimated]);
      this.phraseToSay = "";
    },
    sayPhraseKeyPress(event) {
      if (event.key == "Enter") this.sayPhrase();
    }
  }
};
</script>


<style scoped>
.contents {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
