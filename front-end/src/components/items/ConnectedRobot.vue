<template>
    <div>
          <span class="name">{{robot.name}}</span>
          <span class="ip">{{robot.ipAddress}}</span>
          <span class="id">{{robot.sessionId}}</span>
          <span class="status">Connected</span>
    </div>


</template>



<script>
export default {
  props: ["robot"]
};
</script>
