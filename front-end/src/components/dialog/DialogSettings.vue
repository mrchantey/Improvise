<template>
        <module-item v-bind:title="'Settings'">
        <div class="contents">
            <input-checkbox 
            v-bind:title="'Enabled'" 
            v-bind:onChange="webSpeech.setEnabled" 
            v-bind:initialValue="webSpeech.hasStarted" >
            </input-checkbox>
            <input-checkbox 
            v-bind:title="'Auto Restart'" 
            v-bind:initialValue="webSpeech.autoRestart"  
            v-bind:onChange="webSpeech.setAutoRestart" 
            >
            </input-checkbox>
            <input-checkbox 
            v-bind:title="'Continuous'" 
            v-bind:initialValue="webSpeech.recognition.continuous"  
            v-bind:onChange="webSpeech.setContinuous" 
            >
            </input-checkbox>
            <input-checkbox 
            v-bind:title="'Interim'"   
            v-bind:initialValue="webSpeech.recognition.interimResults"  
            v-bind:onChange="webSpeech.setInterim" 
            >
            </input-checkbox>
            <input-range
            v-bind:title="'Phrase Timeout (not yet implemented)'"
            v-bind:onUp="webSpeech.incrementPhraseTimeout"
            v-bind:onDown="webSpeech.decrementPhraseTimeout"
            v-bind:value="webSpeech.phraseTimeout"
            >
            </input-range>
        </div>
    </module-item>
</template>


<script>
import ModuleItem from "../items/ModuleItem.vue";
import InputCheckbox from "../items/InputCheckbox.vue";
import InputRange from "../items/InputRange.vue";

export default {
  props: ["webSpeech"],
  components: {
    ModuleItem,
    InputCheckbox,
    InputRange
  }
};
</script>


<style scoped>
.contents {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.contents > div {
  font-size: 0.5em;
}
</style>
