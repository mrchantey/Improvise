const play = require('audio-play')
const load = require('audio-loader')

load('last_sentence.wav').then(play).catch(err => console.log(err))

// // const Player = require('player')
// const Player = require('web-audio-player')
// // const Player = 
// const player = Player('testSpeech.mp3')

// player.on('load', () => {
//     console.log('audio loaded..');
//     player.play()
//     player.node.connect(player.context.destination)
// })
// player.on('ended', () => {
//     clg('audio ended')

// })

// console.log('bang');
// // const player = new Player()

// // player.on('playing', (item) => console.log(`started playing ${item}`))
// // player.on('playend', (item) => console.log(`stopped playing ${item}`))
// // player.on('error', (item) => console.log(`error: ${item}`))


// // if (require.main === module) {
// //     player.add('testSpeech.mp3')
// //     console.log(player.list);
// //     console.log('sync start');
// //     console.log('sync end');

// // }