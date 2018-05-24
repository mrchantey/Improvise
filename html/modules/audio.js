
Vue.component('audio-module', {
    props: ['audio'],
    template: `
        <div class="module" v-if="audio !== undefined">
            <div class="module-header">Audio</div>
            <div class="module-content">
                <module-item-range 
                v-bind:obj="audio.Volume"> 
                </module-item-range>
            </div>
        </div>
    `
})

