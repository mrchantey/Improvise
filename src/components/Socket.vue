<template>
<div>socket

<input v-model="message">
<button v-on:click="onSubmit"> Submit</button>

</div>
</template>

<script>
import io from "socket.io-client";

export default {
  name: "Socket",
  data() {
    const data = {
      socket: undefined,
      message: ""
    };
    return data;
  },
  methods: {
    onSubmit() {
      this.socket.send(this.message);
      this.message = "";
    }
  },
  created() {
    this.socket = io("http://localhost:5000");

    this.socket.on("connect", function() {
      console.log("connected!");
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
