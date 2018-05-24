
Vue.component('autonomy-module', {
    props: ['autonomy'],
    template: `
        <div class="module" v-if="autonomy !== undefined">
            <div class="module-header">Autonomy</div>
            <div class="module-content">
                <div class="module-item">
                    <div class="module-item-title">Current State: {{autonomy.State}}</div>
                    <div class="module-item-setting">
                    </div>
                </div>
                <div class="module-item">
                    <button v-on:click="onReset">Reset</button>  
                    <button v-on:click="onToggleState">{{autonomy.State === "disabled" ? "Wake Up": "Go To Sleep"}}</button>
                </div>
                <!-- <div class="module-item">
                    <div>Idle Animations</div>
                    <div>{{autonomy.State}}</div>
                    <div class="module-item-setting">
                        <i v-if="idleAnimPlaying === false"  class="fa fa-play" v-on:click="onToggleIdleAnim"></i>
                        <i v-if="idleAnimPlaying === true" class="fa fa-pause" v-on:click="onToggleIdleAnim"></i>
                    </div>
                </div> -->
            </div>
        </div>
    </div>
  `,
    data() {
        const component = this;
        const data = {
            idleAnimPlaying: false,
            idleAnimIntervalMin: 10,
            idleAnimIntervalMax: 30,
            timeoutId: -1,
            // onStop() {
            //     if (debug) console.log('stopping all behaviors...')
            //     component.session.BehaviorManager.StopAllBehaviors()
            // },
            onReset() {
                component.autonomy.Reset()
            },
            onToggleState() {
                if (component.autonomy.State === "disabled") {
                    component.autonomy.SetState("solitary")
                } else {
                    component.autonomy.SetState("disabled")
                }
            },
            onToggleIdleAnim() {
                if (!component.idleAnimPlaying) {
                    const anims = component.session.BehaviorManager.Behaviors.IdleAnimations;
                    RunIdleAnimation();
                    function RunIdleAnimation() {
                        const behavior = anims[Math.floor(Math.random() * anims.length)]
                        component.session.BehaviorManager.RunBehavior(behavior)

                        const delay = RandomRange(component.idleAnimIntervalMin, component.idleAnimIntervalMax) * 1000
                        component.timeoutId = setTimeout(RunIdleAnimation, delay)
                    }

                    function RandomRange(min, max) {
                        return Math.random() * (max - min) + min
                    }
                } else {
                    clearTimeout(component.timeoutId)
                }
                component.idleAnimPlaying = !component.idleAnimPlaying;
            }
        };
        return data;
    }
})


