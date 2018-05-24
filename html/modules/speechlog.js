
Vue.component('speech-log', {
    props: ['log'],
    template: `
    <div class="module-item">
        <div class="module-item-title">Speech Log</div>
        <!-- <div class="module-item-value">{{behavior.contents.length === 0 ? "behavior" : "folder"}}</div> -->
        <div class="module-item-setting">
            <i v-if="collapsed" class="fa fa-chevron-right" v-on:click="collapsed = !collapsed"></i>
            <i v-if="!collapsed" class="fa fa-chevron-down" v-on:click="collapsed = !collapsed"></i>
            <button v-on:click="clearLog">Clear</button>
        </div>
        <div class="module-item-content" v-if="!collapsed">
            <div id="speech-log" class="speech-log">
            
            <div v-for="(phrase,index) in log"
                v-bind:key="index"
                >{{phrase}}</div>
                <!-- <br><br><br><br><br><br><br><br> -->
            </div>    
        </div>

    </div>
    `,
    data() {
        const component = this
        const data = {
            collapsed: true,
            clearLog() {
                log = []
            }
        }
        return data
    }

})