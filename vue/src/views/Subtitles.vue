<template lang="pug">
  PageContent(title="Subtitles")
    div.container
      div.phrase(
        v-for="(phrase,index) in phrases"
        v-bind:key="index"
      ) {{phrase}}
      p Autoscroll
      input(type="checkbox" v-model="autoscroll")
</template>


<script>
import PageContent from "../components/PageContent.vue";
import EventPoller from "../js/EventPoller.js";

export default {
  components: {
    PageContent
  },
  created() {
    EventPoller.AddPhraseListener(this.UpdatePhrases);
  },
  destroyed(){
    EventPoller.RemovePhraseListener(this.UpdatePhrases);
  },
  data() {
    return {
      phrases: Array,
      // robot: window.$apiInterface.robot,
      autoscroll: true
    };
  },
  methods: {
    // onAutoscrollChange(val) {
    //   this.autoscroll = val;
    // },
    UpdatePhrases(phrases) {
      this.phrases = phrases;
      this.OnPhraseUpdate();
    },
    OnPhraseUpdate() {
      if (this.autoscroll) {
        window.scrollTo({
          top: document.body.scrollHeight,
          behavior: "smooth"
        });
      }
    }
  },
  updated() {}
};
</script>

<style scoped>
.container {
  margin-bottom: 10em;
}

.phrase {
  padding: 0.5em;
  margin: 0.5em;
  background-color: #eeeeee;
}
</style>
