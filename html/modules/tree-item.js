
Vue.component('tree-item', {
    props: ['item', 'oninvoke'],
    template: `
    <div class="tree-item">
        <div class="tree-item-title">{{item.name}}</div>
        <i class="tree-item-run fa fa-play"v-if="item.contents.length === 0" v-on:click="invoke"></i>
        <i class="tree-item-collapse fa fa-chevron-right" v-if="collapsed && item.contents.length !== 0" v-on:click="collapsed = !collapsed"></i>
        <i class="tree-item-collapse fa fa-chevron-down" v-if="!collapsed && item.contents.length !== 0" v-on:click="collapsed = !collapsed"></i>
    
        <div class="tree-item-content" v-if="!collapsed">
            <tree-item 
                v-for="(subitem,index) in item.contents"
                v-bind:item="subitem"
                v-bind:key="index"            
                v-bind:oninvoke="oninvoke"
            ></tree-item>
        </div>

    </div>
    `,
    data() {
        const component = this
        const data = {
            collapsed: true,
            invoke() {
                component.oninvoke(component.item)
            }
        }
        return data
    }

})