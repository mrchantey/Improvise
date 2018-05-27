<template>
<div>
    <h1>Home</h1>
    <div>Welcome to the Nao Controller app. To get started, please enter the ip address below</div>
    <input v-model="naoIP" @keydown="ipKeyDown">
    <button @click="submit">Submit</button>
</div>
</template>

<script>
export default {
  data() {
    return {
      naoIP: ""
    };
  },
  methods: {
    submit() {
      this.$router.push("/socket/" + this.naoIP);
      this.naoIP = "";
    },
    ipKeyDown(event) {
      if (event.key === "Enter") this.submit();
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
