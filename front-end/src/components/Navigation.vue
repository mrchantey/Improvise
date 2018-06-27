<template>
    <div>
      <hr>
      <div class="container">
        <div class="links">
          <router-link to="/">Home</router-link>
          <router-link to="/connection">Connection</router-link>
          <router-link to="/remote">Remote</router-link>
          <router-link to="/actions">Actions</router-link>
          <router-link to="/dialog">Dialog</router-link>
          <!-- <router-link to="/settings">Settings</router-link> -->
          <router-link to="/subtitles">Subtitles</router-link>
        </div>
      </div>
      <hr>
    </div>


</template>

<style scoped>
.container {
  display: grid;
  grid-template-columns: 1fr minmax(5em, 50em) 1fr;
}
.links {
  text-align: center;
  display: grid;
  font-size: 0.9em;
  grid-column-start: 2;
  grid-column-end: 3;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
}
</style>