<template>
<div>
    <module v-bind:title="'Dialog'">
      <dialog-settings v-bind:webSpeech="webSpeech"></dialog-settings>
      <dialog-status v-bind:webSpeech="webSpeech"></dialog-status>
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
