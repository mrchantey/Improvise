
Vue.component('speech-module', {
    props: ['speech'],
    template: `
    <div class="module" v-if="speech !== undefined">
        <div class="module-header">Speech</div>
        <div class="module-content">
            <module-item-range v-bind:obj="speech.Volume"></module-item-range>
            <module-item-range v-bind:obj="speech.Speed"></module-item-range>
            <module-item-range v-bind:obj="speech.Pitch"></module-item-range>

            <div class="module-item">
                <div>Current Sentence: {{speech.currentSentence}}</div>
                <div>
                    <i class="fa fa-pause" v-on:click="onStop" ></i>
                </div>
            </div>
            <div class="module-item">
                <div>Say A Phrase</div>
                <div>
                    <textarea v-on:keydown="onKeyPress" id="sayInput" tabindex="2" v-model="phrase"></textarea>
                </div>
                    <div class="module-item-setting">
                <div>
                <input type="checkbox" v-model:checked="speech.animate">Animate</input>
                </div>
                <i class="fa fa-play run-behavior"  v-on:click="sayPhrase"></i>
                </div>
            </div>
            <speech-log v-bind:speech='speech.log'></speech-log>       
            <text-item class="module-item"
            v-for="(text,index) in preparedText"
            v-bind:key="index"
            v-bind:onsay="sayText"
            v-bind:text="text"
            >  
        </text-item>
        </div>
    </div>
  `,
    data() {
        const component = this
        const data = {
            log: '',
            phrase: "hi there",
            preparedText: g_preparedText,
            sayPhrase() {
                component.sayText(component.phrase)
            },
            sayText(text) {
                component.speech.Say(text)
                component.phrase = ''
                document.getElementById('sayInput').value = ''
            },
            onKeyPress(event) {
                if (event.key === "Enter")
                    component.sayPhrase()
            },
            onStop() { component.speech.Stop() },
            onSpeedUp() { component.speech.speed += 10 },
            onSpeedDown() { component.speech.speed -= 10 }
        };
        return data;
    },
    created() {
    }

})



