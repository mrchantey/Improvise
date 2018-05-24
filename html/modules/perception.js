
Vue.component('perception-module', {
    props: ['perception'],
    template: `
        <div class="module" v-if="perception !== undefined">
            <div class="module-header">People Perception</div>
            <div class="module-content">
                <!-- <div class="module-item" v-if="session.AudioDevice.Volume !== undefined">
                    <div class="module-item-title">Volume</div>
                    <div class="module-item-value">{{session.AudioDevice.Volume}}</div>
                    <div class="module-item-setting">
                        <i class="fa fa-minus" v-on:click="onVolumeDown"></i>
                        <i class="fa fa-plus" v-on:click="onVolumeUp"></i>
                     </div>
                </div> -->
            </div>
        </div>
  `,
    data() {
        const component = this;
        const data = {
        };

        return data;
    }
})
