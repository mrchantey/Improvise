<template>
  <div id="app">
  
    <heading></heading>
    <navigation></navigation>
    <router-view/>
  </div>
</template>

<script>
import Heading from "./components/Heading.vue";
import Navigation from "./components/Navigation.vue";

export default {
  name: "App",
  components: {
    Heading,
    Navigation
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Montserrat:400,700");
/* @import "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"; */

body {
  background-color: #f7f7f7;
}

#app {
  font-family: "Montserrat", sans-serif;
  /* font-family: "Avenir", Helvetica, Arial, sans-serif; */
  /* -webkit-font-smoothing: antialiased; */
  /* -moz-osx-font-smoothing: grayscale; */
  /* text-align: center; */
  /* color: #2c3e50; */
  /* margin-top: 60px; */
}

button {
  font-size: 1em;
  padding: 0.2em;
}
</style>
