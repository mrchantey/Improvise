<template lang="pug">
  PageContent(title="Raw Command")
    p.sectionTitle Raw Command
    InputTextArea(v-bind:submitCallback="submitCommandCallback")
</template>



<script>
import InputTextArea from "../../components/InputTextArea.vue";
import PageContent from "../../components/PageContent.vue";
import NaoServer from "../../js/NaoServer";
import Vue from "vue";
export default Vue.extend({
  data() {
    return {
      submitCommandCallback: NaoServer.ServerRequest
      // submitCommandCallback: Function
      // submitCommandCallback: window.$ServerRequest
    };
  },
  components: {
    PageContent,
    InputTextArea
  }
});
</script>
