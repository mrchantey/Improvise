<template>
       <module-item v-bind:title="'Conversation'">
           <input-text
           v-bind:title="'Ask a question'"
           v-bind:onEnterCallback="webSpeech.MakeQuery">
           </input-text>
           
           <div class="contents">
            <div v-for="(sentence,index) in webSpeech.conversationLog"
            v-bind:key="index"
            v-bind:class="'sentence ' + sentence.type"
            >{{sentence.text}}</div>
           </div>
        </module-item>
</template>


<script>
import ModuleItem from "../items/ModuleItem";
import InputText from "../items/InputText";
export default {
  props: ["webSpeech"],
  components: {
    InputText,
    ModuleItem
  }
};
</script>


<style>
.contents {
  display: grid;
  grid-template-columns: 0.1fr 0.8fr 0.1fr;
}

.sentence {
  padding: 0.5rem;
  margin: 0.5em;
}
.query {
  background-color: greenyellow;
  grid-column-start: 2;
  grid-column-end: 4;
}
.response {
  background-color: #eeeeee;
  grid-column-start: 1;
  grid-column-end: 3;
}
</style>
