<template>
    <div>
      <hr>
      <div class="links">
      <!-- <router-link to="/">Home</router-link> -->
      <router-link to="/connection">Connection</router-link>
      <router-link to="/dialog">Dialog</router-link>
      <router-link to="/remote">Remote Controller</router-link>
      <!-- <router-link to="/settings">Settings</router-link> -->
      <router-link to="/actions">Actions</router-link>
      <router-link to="/subtitles">Subtitles</router-link>
      </div>
      <hr>
    </div>


</template>

<style scoped>
div {
  text-align: center;
}
.links {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
}
</style>