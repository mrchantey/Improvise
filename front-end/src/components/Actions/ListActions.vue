<template>

<div>
        <div
            v-for="(behavior,index) in robot.behaviors"
        v-bind:key="index"
                
        ></div>
</div>





</template>



<script>
export default {
  props: ["robot"]
};
</script>
