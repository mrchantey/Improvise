Vue.component('module-item-range', {
    props: ['obj'],
    template: `
    <div class="module-item number" v-if="obj.value !== undefined">
        <div>{{obj.name}}: {{obj.value}}</div>
        <div>
            <input v-model.number="obj.value" type="range" v-bind:min="obj.min" v-bind:max="obj.max" v-on:input="oninput">
        </div>
    </div>
    `,
    data() {
        const component = this;
        const data = {
            sldValue: 0
        }
        data.oninput = () => component.obj.set(component.obj.value)
        return data
    }
})