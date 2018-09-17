<template lang="pug">
  div(id="app")
    heading
    navigation
    router-view
</template>

<script>
import Heading from "./views/Heading.vue";
import Navigation from "./views/Navigation.vue";

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

body {
  background-color: #f7f7f7;
}

#app {
  /* font-family: "Avenir", Helvetica, Arial, sans-serif; */
  font-family: "Montserrat", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
/* #nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
