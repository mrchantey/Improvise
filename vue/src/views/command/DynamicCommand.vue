<template lang="pug">
  PageContent(title="Dynamic Command")
    div
      button(@click="OnDownload") Download
      button(@click="OnUpload") Upload
    span.setting
      p.name presets
      select.value(
        v-model="selectedPresetName"
        @change="OnPresetUpdate")
        option(
          v-for="(preset,index) in presets"
          v-bind:key="index")
          p {{preset.name}}
    span.setting
      p.name Title
      input.value(v-model="title")
    button(@click="OnSubmit") Submit
    TypedCommand(v-bind:command="command", v-bind:depth="0")
</template>




<script lang="ts">
import PageContent from "../../components/PageContent.vue";
import NaoServer from "../../js/NaoServer.js";
import CommandUtility from "../../js/CommandUtility.js";
import TypedCommand from "./TypedCommand.vue";
import Vue from "vue";
export default Vue.extend({
  components: {
    PageContent,
    TypedCommand
  },
  data() {
    // console.log(CommandUtility.GetCommandPresets());
    const presets = CommandUtility.GetCommandPresets();
    return {
      command: CommandUtility.CommandBodyToCommandFields(presets[0]),
      // command: { fields: [] },
      presets: presets,
      selectedPresetName: presets[0].name,
      title: presets[0].name
    };
  },
  // created() {
  //   this.OnPresetUpdate();
  // },
  methods: {
    OnSubmit() {
      const commandBody = CommandUtility.CommandFieldsToCommandBody(
        this.command
      );
      NaoServer.ServerRequest(commandBody);
      // console.log(simpleCommand);
    },
    OnDownload() {
      const commandBody = CommandUtility.CommandFieldsToCommandBody(
        this.command
      );
      commandBody.name = this.title;
      CommandUtility.DownloadCommandBody(commandBody);
    },
    OnUpload() {
      CommandUtility.UploadCommandBodyAsync().then(commandBody => {
        this.command = CommandUtility.CommandBodyToCommandFields(commandBody);
        this.title =
          commandBody.name === undefined
            ? "Uploaded Command"
            : commandBody.name;
      });
    },
    OnPresetUpdate() {
      this.command = CommandUtility.CommandBodyToCommandFields(
        this.presets.find(p => p.name === this.selectedPresetName)
      );
      this.title = this.selectedPresetName;
      CommandUtility.FilterCommand(this.command);
    }
  }
});
</script>



<style scoped>
.setting {
  display: grid;
  grid-template-columns: 1fr 1fr;
  max-width: 30em;
}

.setting > .name {
  grid-column: 1;
}

.setting > .value {
  grid-column: 2;
  /* max-height: 2em; */
  align-self: center;
}
</style>
