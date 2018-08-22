const fs = require('fs')
const axios = require('axios')

const baseUrl = 'https://api.openweathermap.org/data/2.5/weather'
const apiKey = fs.readFileSync(__dirname + '/keys/weatherAPIKey.txt')
const city = 'Sydney'
const url = baseUrl + '?q=' + city + "&APPID=" + apiKey


const KELVIN = 273.15

exports.RequestConversationalWeather = function () {
    return new Promise((resolve, reject) => {
        exports.RequestWeather()
            .then(data => {
                const description = data.weather[0].description;
                // const temp = Math.round(data.main.temp)
                const temp = Math.round(data.main.temp - KELVIN)
                const phrase = `Today we can expect ${description}. The Temperature outside is ${temp} degrees.`
                resolve(phrase)
            })
            .catch()
    })
}


exports.RequestWeather = function () {
    return new Promise((resolve, reject) => {
        axios.get(url)
            .then((result) => {
                // console.log(result);
                resolve(result.data)
            }).catch((err) => {
                console.error(err);
                reject(err)
            });
    })
}

if (require.main === module) {
    // console.log(url);
    // exports.RequestWeather()
    exports.RequestConversationalWeather()
        .then(res => console.log(res))
    // .then(res => {
    //     for (var prop in res.data) {
    //         console.log(prop);
    //     }

    // })

}