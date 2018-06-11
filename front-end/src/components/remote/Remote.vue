<template>
<div v-if="robot.isConnected === true">
  <module 
  v-bind:title="robot.name+ ' Remote Controller'">
  <div class="contents">
  <input-range 
  v-bind:title="'Volume'"
  v-bind:onDown="volumeDown"
  v-bind:onUp="volumeUp"
  v-bind:value="robot.volume"
  ></input-range>
  <module-item v-bind:title="'Buttons'">
    <button @click="wakeUp">Wake Up</button>
    <button @click="goToSleep">Go To Sleep</button>
  </module-item>
  <module-item v-bind:title="'Say A Phrase'">
    <input @keypress="sayPhraseKeyPress" v-model="phraseToSay">
    <button @click="sayPhrase">Say</button>
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
      robot: window.$apiInterface.robot
    };
  },
  methods: {
    volumeDown() {
      this.robot.SetProperty("volume", this.robot.volume - 10);
    },
    volumeUp() {
      this.robot.SetProperty("volume", this.robot.volume + 10);
    },
    wakeUp() {
      this.robot.DoMethod("SetAutoState", "solitary");
    },
    goToSleep() {
      this.robot.DoMethod("SetAutoState", "disabled");
    },
    sayPhrase() {
      this.phraseToSay = "";
      this.robot.DoMethod("SayPhrase", this.phraseToSay);
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

.contents > * {
  padding: 1em;
}
</style>
