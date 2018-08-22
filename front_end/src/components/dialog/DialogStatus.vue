<template>
    <module-item v-bind:title="'Status'">
    <div class='contents'>
        <output-text v-bind:title="'Current Sentence'" v-bind:value="webSpeech.currentSentence"></output-text>
        <output-text v-bind:title="'Last Sentence'" v-bind:value="webSpeech.lastSentence"></output-text>
        <output-checkbox v-bind:title="'Online'" v-bind:value="webSpeech.hasStarted"></output-checkbox>
        <output-checkbox v-bind:title="'Audio Online'" v-bind:value="webSpeech.hasAudioStarted"></output-checkbox>
        <output-checkbox v-bind:title="'Sound detected'" v-bind:value="webSpeech.hasSoundStarted"></output-checkbox>
        <output-checkbox v-bind:title="'Speech detected'" v-bind:value="webSpeech.hasSpeechStarted"></output-checkbox>
    </div>
    </module-item>
</template>




<script>
import OutputText from "../items/OutputText.vue";
import OutputCheckbox from "../items/OutputCheckbox.vue";
import ModuleItem from "../items/ModuleItem.vue";

export default {
  props: ["webSpeech"],
  components: {
    ModuleItem,
    OutputText,
    OutputCheckbox
  }
};
</script>


<style scoped>
.contents {
  display: grid;
  grid-template-columns: 1fr 1fr;
  font-size: 0.7em;
}
</style>

