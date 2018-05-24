Vue.component('listen-module', {
    props: ['listen'],
    template: `
    <div class="module" v-if="listen !== undefined">
        <div class="module-header">Listening</div>
        <div class="module-content">
            <div class="module-item">
                <div>Enable Listening Beeps</div>
                <input type="checkbox" v-model:checked="listen.ListenBeeps"v-on:click="ToggleListenBeeps"></input>
            </div>
        </div>
    </div>
  `,
    data() {
        const component = this
        const data = {
            ToggleListenBeeps() {
                component.listen.ToggleListenBeeps()
            }

        }
        return data;
    }
})