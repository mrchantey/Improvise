<template>
<div>socket
<div>Nao Ip address: {{$route.params.naoIP}}</div>

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
  methods: {},
  created() {
    this.socket = io("http://localhost:5000");

    this.socket.on("connect", function() {
      console.log("connected!");
    });

    this.socket.on("message", function(msg) {
      console.log("message from server: " + msg);
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
