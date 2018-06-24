<template>
<div>
    <module v-bind:title="'Dialog'">
        <module-item v-bind:title="'Settings'">
            <input-checkbox 
            v-bind:title="'Enabled'" 
            v-bind:onChange="setEnabled" 
            v-bind:initialValue="webSpeech.hasStarted" >
            </input-checkbox>
            <input-checkbox 
            v-bind:title="'Auto Restart'" 
            v-bind:initialValue="webSpeech.autoRestart"  
            v-bind:onChange="setAutoRestart" 
            >
            </input-checkbox>
            <input-checkbox 
            v-bind:title="'Continuous'"   
            v-bind:onChange="webSpeech.setContinuous" 
            >
            </input-checkbox>
            <input-checkbox 
            v-bind:title="'Interim'"   
            v-bind:onChange="webSpeech.setInterim" 
            >
            </input-checkbox>
            
            
            Enabled,Continuous,Interim,PhraseTimeout
        </module-item>
        <module-item v-bind:title="'Status'">
            <output-text v-bind:title="'Current Sentence'" v-bind:value="webSpeech.currentSentence"></output-text>
            <output-text v-bind:title="'Last Sentence'" v-bind:value="webSpeech.lastSentence"></output-text>
            <output-text v-bind:title="'Current Sentence'" v-bind:value="webSpeech.currentSentence"></output-text>
            <output-checkbox v-bind:title="'Online'" v-bind:value="webSpeech.hasStarted"></output-checkbox>
            <output-checkbox v-bind:title="'Audio Online'" v-bind:value="webSpeech.hasAudioStarted"></output-checkbox>
            <output-checkbox v-bind:title="'Sound detected'" v-bind:value="webSpeech.hasSoundStarted"></output-checkbox>
            <output-checkbox v-bind:title="'Speech detected'" v-bind:value="webSpeech.hasSpeechStarted"></output-checkbox>
        </module-item>
        <module-item v-bind:title="'Conversation'">
            <div v-for="(sentence,index) in webSpeech.speechLog"
            v-bind:key="index"
            >{{sentence}}</div>
        </module-item>   
    </module>
</div>
</template>


 <script>
import Module from "../items/Module.vue";
import ModuleItem from "../items/ModuleItem.vue";
import InputCheckbox from "../items/InputCheckbox.vue";
import InputRange from "../items/InputRange.vue";
import OutputText from "../items/OutputText.vue";
import OutputCheckbox from "../items/OutputCheckbox.vue";

export default {
  components: {
    Module,
    ModuleItem,
    InputCheckbox,
    InputRange,
    OutputText,
    OutputCheckbox
  },
  data() {
    return {
      webSpeech: window.$webSpeechInterface
    };
  },
  methods: {
    setAutoRestart(val) {
      this.webSpeech.autoRestart = val;
    },
    setEnabled(val) {
      if (val) this.webSpeech.start();
      else this.webSpeech.stop();
    }
  }
};
</script>