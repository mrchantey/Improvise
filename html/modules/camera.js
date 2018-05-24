
Vue.component('camera-module', {
    props: ['camera'],
    template: `
        <div class="module" v-if="camera !== undefined">
            <div class="module-header">Photo Capture</div>
            <div class="module-content">
                <div class="module-item">
                    <!-- <div class="module-item-title">Path</div>
                    <div class="module-item-value">
                        <input v-model="path"></input> 
                    </div> -->
                    <div class="module-item-setting">
                        <button v-on:click="onCapture">Take Photo</button>
                        <button v-on:click="onDownload">Download Photo</button>
                     </div>
                     <div class="module-item-content">
                         <img id="last-photo" alt="Last Photo Taken">
                     </div>
                </div>
            </div>
        </div>
  `,
    data() {
        const component = this;
        const data = {
            // path: "/Documents/GitHub/nao-controller/html/img1.jpg",
            path: "",
            onCapture() {
                component.camera.TakePhoto("img1")
            },
            onDownload() {
                component.nao.DownloadPhoto("img1.jpg")
            }
        };

        return data;
    }
})


