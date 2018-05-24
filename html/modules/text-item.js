
Vue.component('text-item', {
    props: ['text', 'onsay'],
    template: `
    <div class="module-item">
        <div class="module-item-title" style="grid-column: 1 / 3;">{{text.name}}</div>
        <div class="module-item-setting">
            <button v-on:click="Say">Say</button>
        </div>
    </div>
    `,
    data() {
        const component = this
        const data = {
            Say() {
                component.onsay(component.text.content)
            }
        }
        return data
    }

})