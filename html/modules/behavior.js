
Vue.component('behavior-module', {
    props: ['behavior'],
    template: `
        <div class="module" v-if="behavior !== undefined">
            <div class="module-header">Behaviors</div>
            <div class="module-content">
                <!-- <div class="module-item" >
                    <div v-if="behavior.currentBehavior !== undefined">Current Behavior: {{behavior.currentBehavior.name}}</div>
                </div>
                <div class="module-item">
                        <i 
                        v-if="behavior.currentBehavior !== 'none' " 
                        class="fa fa-pause" 
                        v-on:click="onStop" ></i>
                </div> -->
                <div class="module-item">
                <tree-item 
                v-if="behavior.Behaviors !== undefined"
                v-bind:item="behavior.Behaviors.All"
                v-bind:oninvoke="onRun"
                ></tree-item>
                </div>
            </div>
        </div>
  `,
    data() {
        const component = this;
        const data = {
            onRun(behavior) {
                component.behavior.RunBehavior(behavior)
            },
            onStop() {
                component.behavior.StopBehavior(component.behavior.CurrentBehavior)
            }
        };
        return data;
    }

})


