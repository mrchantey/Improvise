<template>
<div>Subtitles
    <div>{{speechLog}}</div>
</div>
</template>


<script>
export default {
  data() {
    return {
      speechLog: window.$apiInterface.robot.speechLog
    };
  }
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
