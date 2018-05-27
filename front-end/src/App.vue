<template>
  <div id="app">
  
    <nao-header></nao-header>
    <hr>
    <router-link to="/">Home</router-link>
    <router-link to="/subtitles">Subtitles</router-link>
    <router-link to="/socket/69">Socket Test</router-link>
    <hr>

    <!-- <img src="./assets/logo.png"> -->
    <router-view/>
  </div>
</template>

<script>
import NaoHeader from "./components/NaoHeader.vue";

export default {
  name: "App",
  components: {
    NaoHeader
  }
};
</script>

<style>
/* #app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
