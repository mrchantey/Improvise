<template lang="pug">
    div(class="navigation")
        hr
        div(class="container")
            div(class="links")
                //- router-link(to="/") Home
                router-link(to="/dynamiccommand") Dynamic Command
                router-link(to="/rawcommand") Raw Command
        hr
</template>


<style scoped>
.container {
  display: grid;
  grid-template-columns: 1fr minmax(5em, 50em) 1fr;
}
.links {
  font-size: 0.9em;
  background-color: #ffffff;
  display: grid;
  grid-column-start: 2;
  grid-column-end: 3;
  grid-template-columns: 1fr 1fr;
}
</style>
