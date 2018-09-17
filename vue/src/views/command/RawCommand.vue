<template lang="pug">
    PageItem(title="Raw Command")
      InputText(v-bind:submitCallback="submitCommandCallback")

</template>



<script>
import PageItem from "../../components/PageItem.vue";
import InputText from "../../components/InputText.vue";
import Vue from "vue";
export default Vue.extend({
  data() {
    return {
      // submitCommandCallback: Function
      submitCommandCallback: window.$ServerRequest
    };
  },
  components: {
    PageItem,
    InputText
  }
});
</script>
