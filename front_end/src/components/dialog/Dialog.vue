<template>
<div>
    <module v-bind:title="'Dialog'">
      <dialog-settings v-bind:webSpeech="webSpeech"></dialog-settings>
      <hr>
      <dialog-status v-bind:webSpeech="webSpeech"></dialog-status>
      <hr>
      <dialog-conversation v-bind:webSpeech="webSpeech"></dialog-conversation>
    </module>
</div>
</template>


 <script>
import Module from "../items/Module.vue";
import DialogConversation from "./DialogConversation";
import DialogSettings from "./DialogSettings";
import DialogStatus from "./DialogStatus";

export default {
  components: {
    Module,
    DialogConversation,
    DialogSettings,
    DialogStatus
  },
  data() {
    return {
      webSpeech: window.$webSpeechInterface
    };
  }
};
</script>
