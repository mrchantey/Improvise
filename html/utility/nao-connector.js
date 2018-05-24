

function BeginNaoSession(ipAddress, callback) {
    console.log("Connecting...")

    //qimessaging 1
    const session = naoDeployed ? new QiSession() : new QiSession(ipAddress)
    session.socket()
        .on('connect', onSessionConnect(session, callback))
        .on('disconnect', onSessionDisconnect())

    function onSessionConnect(session, connectedCallback) {
        console.log('QiSession connected!');


        const services = [
            { name: "ALMemory", callback: (s) => session.Memory = s },
            { name: "ALAudioDevice", callback: (s) => session.AudioDevice = s },
            { name: "ALAudioPlayer", callback: (s) => session.AudioPlayer = s },
            { name: "ALAnimatedSpeech", callback: (s) => session.AnimatedSpeech = s },
            { name: "ALAutonomousLife", callback: (s) => session.AutonomousLife = s },
            { name: "ALBehaviorManager", callback: (s) => session.BehaviorManager = s },
            { name: "ALPeoplePerception", callback: (s) => session.PeoplePerception = s },
            { name: "ALPhotoCapture", callback: (s) => session.PhotoCapture = s },
            { name: "ALSpeechRecognition", callback: (s) => session.SpeechRecognition = s },
            { name: "ALTextToSpeech", callback: (s) => session.TextToSpeech = s },
            { name: "ALVideoDevice", callback: (s) => session.VideoDevice = s }
        ]

        ConnectServices()

        function ConnectServices() {

            let connectedServiceCount = 0;
            for (let i = 0; i < services.length; i++) {
                ConnectService(services[i].name, services[i].callback)
            }

            function ConnectService(serviceName, callback) {
                session.service(serviceName).done(service => {
                    console.log(serviceName + " Connected!")
                    callback(service)
                    connectedServiceCount++;
                    if (connectedServiceCount >= services.length)
                        OnServicesConnected()
                }).fail(onFail)
            }

        }

        function OnServicesConnected() {
            console.log(services.length + " Services Connected")
            CreateNaoJS()
        }

        function CreateNaoJS() {

            function SubscribeToEvent(eventName, callback) {
                session.Memory.subscriber(eventName).done(s => {
                    s.signal.connect(callback)
                })
            }

            const nao = {}
            nao.Audio = CreateAudioModule()
            nao.Autonomy = CreateAutonomyModule()
            nao.Behavior = CreateBehaviorModule()
            nao.Camera = CreateCameraModule()
            nao.Listen = CreateListenModule()
            nao.Perception = CreatePerceptionModule()
            nao.Speech = CreateSpeechModule()

            callback(nao)

            function CreateNumberProperty(name, min, max, get, set) {
                const prop = {
                    value: undefined,
                    name: name,
                    min: min,
                    max: max,
                    get: get
                }
                prop.get = () => get().done((val) => prop.value = val).fail(onFail)
                prop.set = (val) => set(val).done(() => prop.get()).fail(onFail)
                prop.get()
                return prop
            }

            function CreateAudioModule() {
                const aup = session.AudioPlayer;
                // aup.loadFile('/home/nao/recordings/king.wav').done((id) => {
                //     console.log('load successful: ' + id)
                //     aup.play(id).done((msg) => {
                //         console.log('done playing: ' + id)
                //     })
                // }).fail(onFail)
                const audio = {
                    Volume: CreateNumberProperty(
                        "Master Volume",
                        0,
                        60,
                        session.AudioDevice.getOutputVolume,
                        session.AudioDevice.setOutputVolume
                    )
                }
                audio.Play = (path) =>
                    aup.loadFile(path)
                        .done((id) => {
                            aup.play(id)
                                .done(() =>
                                    aup.unloadFile(id)
                                        .done(() =>
                                            console.log('file unloaded: ' + id)
                                        )
                                        .fail(onFail)
                                )
                                .fail(onFail)
                        })
                        .fail(onFail)
                audio.Stop = () =>
                    aup.stopAll()
                        .done()
                        // aup.unloadAllFiles()
                        //     .done(() =>
                        //         console.log('all files stopped and unloaded'))
                        //     .fail(onFail))
                        .fail(onFail);

                setTimeout(audio.Stop, 3000)
                return audio
            }

            function CreateAutonomyModule() {
                const autonomy = {
                    State: undefined,
                    SetState: session.AutonomousLife.setState,
                }
                autonomy.Reset = () => {
                    session.AutonomousLife.stopAll().done(() => {
                        // console.log('resetting...')
                        autonomy.SetState('disabled').done(() => autonomy.SetState('solitary'))
                        // aul.setState('solitary')
                    })
                }
                session.AutonomousLife.getState().done((s) => autonomy.State = s)
                SubscribeToEvent("AutonomousLife/State", (s) => autonomy.State = s)
                return autonomy
            }

            function CreateBehaviorModule() {
                const bm = session.BehaviorManager
                const behavior = {
                    Behaviors: undefined,
                    currentBehavior: undefined
                }
                bm.getInstalledBehaviors().done(allPaths => {
                    behavior.Behaviors = SortBehaviors(allPaths)
                })

                behavior.RunBehavior = (behavior) => {
                    behavior.currentBehavior = behavior
                    bm.runBehavior(behavior.path).done(() => behavior.currentBehavior = undefined)
                }
                behavior.StopBehavior = (behavior) => {
                    console.log("stopping behavior: " + behavior.name)
                    bm.stopBehavior(behavior.path)
                }

                behavior.StopCurrentBehavior = () => behavior.StopBehavior(behavior.currentBehavior)
                behavior.StopAllBehaviors = bm.stopAllBehaviors
                return behavior
            }

            function CreateCameraModule() {
                const camera = {}
                const pho = session.PhotoCapture
                function DownloadImage(source, destin) {
                    var elt = document.createElement('a')
                    console.log("source: " + source)
                    elt.setAttribute('href', source)
                    elt.setAttribute('download', destin)
                    console.log(elt)
                    elt.style.display = 'none'
                    document.body.appendChild(elt)
                    elt.click();
                    document.body.removeChild(elt)
                }

                camera.TakePhoto = (fileName) => {
                    const path = "/home/nao/.local/share/PackageManager/apps/web/html"
                    console.log("taking photo...")
                    pho.takePicture(path, fileName).done(d => {
                        console.log("photo captured")
                        document.getElementById('last-photo').src = "img1.jpg?random=" + new Date().getTime()
                    })
                }
                //paths are local    ie src = 'img1.jpg' dest= 'Downloaded Image.jpg'
                camera.DownloadPhoto = (src) => DownloadImage(src, "NAO Photo Capture.jpg");
                return camera
            }

            function CreateListenModule() {
                const spr = session.SpeechRecognition
                const listen = {
                    playSound: true//will toggle on start
                }
                listen.ToggleListenBeeps = () => {
                    spr.setAudioExpression(!listen.playSound).done(() =>
                        spr.getAudioExpression().done(val => {
                            listen.playSound = val
                            // console.log('listen beeps enabled: ' + val)
                        }))
                }
                listen.ToggleListenBeeps()
                return listen
            }

            function CreatePerceptionModule() {
                const perception = {
                    OnPeopleDetected: []
                }
                SubscribeToEvent("PeoplePerception/PeopleDetected", (eve) => {
                    // console.log("people detected")
                    // console.log(eve)
                    perception.OnPeopleDetected.forEach(f => f(eve))
                })
                return perception
            }

            function CreateSpeechModule() {
                const tts = session.TextToSpeech
                const ani = session.AnimatedSpeech

                // tts.setParameter("speed", 400).done(v => {
                //     //        console.log('speed set')
                //     //          console.dir(v)
                //     //      tts.getParameter("speed").done(s => console.dir(s))
                // })

                const speech = {
                    Volume: CreateNumberProperty(
                        "Volume",
                        0.001,
                        200,
                        () => { return tts.getParameter("volume") },
                        (val) => { return tts.setParameter("volume", val) }
                    ),
                    Speed: CreateNumberProperty(
                        "Speed",
                        50,
                        400,
                        () => { return tts.getParameter("speed") },
                        (val) => { return tts.setParameter("speed", val) }
                    ),
                    Pitch: CreateNumberProperty(
                        "Pitch",
                        50,
                        200,
                        () => { return tts.getParameter("pitch") },
                        (val) => { return tts.setParameter("pitch", val) }
                    ),
                    animate: true,
                    cancelAll: false,
                    currentSentence: '',
                    log: [],
                    speed: 80
                }

                speech.Say = (paragraph) => {
                    const sentences = SplitAndValidateParagraph(paragraph)
                    IterateSay(0)
                    function IterateSay(i) {
                        //                        const sentence = "\\\\\\\\rspd=" + speech.speed + "\\\\\\\\" + sentences[i]
                        const sayCallback = speech.animate ? ani.say : tts.say
                        //animated speech speed not working
                        console.log("now saying: " + sentences[i])

                        sayCallback(sentences[i]).done(() => {
                            if (speech.cancelAll) {
                                speech.cancelAll = false
                            }
                            else if (i + 1 < sentences.length)
                                IterateSay(i + 1)
                        })
                    }
                }

                speech.Stop = () => {
                    speech.cancelAll = true
                    tts.stopAll()
                }

                SubscribeToEvent("ALTextToSpeech/TextDone", (s) => speech.currentSentence = '')
                SubscribeToEvent("ALTextToSpeech/TextInterrupted", (s) => speech.currentSentence = '')
                SubscribeToEvent("ALTextToSpeech/CurrentSentence", (s) => {
                    if (s === '.')
                        return;
                    speech.currentSentence = s
                    speech.log.push(s)
                })
                return speech
            }

        }

    }
}

function onSessionDisconnect() {
    //     console.log('QiSession disconnected!');
}

function onFail(error) {
    console.log("An error occurred:", error);
}