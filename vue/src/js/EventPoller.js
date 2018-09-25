import "./NaoServer"
import NaoServer from "./NaoServer";


export default {
  BeginSpokenPhrasePolling,
  AddPhraseListener,
  RemovePhraseListener
}

const phraseListeners = []

function AddPhraseListener(callback) {
  const index = phraseListeners.indexOf(callback)
  if (index === -1)
    phraseListeners.push(callback)
}

function RemovePhraseListener(callback) {
  const index = phraseListeners.indexOf(callback)
  if (index !== -1)
    phraseListeners.splice(index, 1)
}


function BeginSpokenPhrasePolling() {
  setInterval(SpokenPhrasePollHandler, 2000)
}

function SpokenPhrasePollHandler() {
  RequestSpokenPhrases().then(phrases => {
    phraseListeners.forEach(l => l(phrases))
  })
}

function RequestSpokenPhrases() {
  return new Promise((resolve, reject) => {
    NaoServer.ServerRequest({
      "commandName": "event",
      "drain": false
    }).then(body => {
      // console.log(body);
      const events = body.response
      const phrases = events
        .filter(e => e.key === 'ALTextToSpeech/CurrentSentence')
        .filter(e => e.value !== '')
        .map(e => e.value)
      resolve(phrases)
    })
  });
}

// function cleanUpSpeech(speech) {
//   const splitSpeech = speech.split('\\')
//   let newSpeech = ''
//   for (let i = 0; i < splitSpeech.length; i += 2) {
//     newSpeech += splitSpeech[i]
//   }
//   return newSpeech
// }

// robot.SetEventListening = (val) => {
//   function FetchEvents(drain) {
//       return new Promise((resolve, reject) => {
//           MakeRequest(naoAddress, { 'module': 'events', 'drain': drain })
//               .then((resBody) => resolve(resBody['events']))
//       })
//   }
//   if (val == true) {
//       robot.eventListeningEnabled = true
//       robot.eventIntervalId = setInterval(() => {
//           FetchEvents(true).then((events) => FilterEvents(robot, events))
//       }, 5000)
//   } else if (robot.eventIntervalId != undefined) {
//       robot.eventListeningEnabled = false
//       clearInterval(robot.eventIntervalId)
//   }
// }

// robot.SetEventListening(true)