import json
import requests
from pkg.utilservices import utility

baseUrl = 'http://api.openweathermap.org/data/2.5/weather'
apiKey = utility.OpenJson('pkg/keys/weatherAPIKey.json')['key']
city = 'Sydney'
url = baseUrl + '?q=' + city + "&APPID=" + apiKey
KELVIN = 273.15


def RequestWeather():
    req = requests.get(url)
    uniData = json.loads(req.text)
    weatherData = utility.parseType(uniData)
    WeatherKelvinToCelsius(weatherData)
    # for key, value in data.iteritems():
    #     print key, value
    return weatherData


def RequestWeatherDescription():
    weather = RequestWeather()
    descr = weather["weather"][0]['description']
    temp = int(round(weather["main"]["temp"]))
    temp_min = int(round(weather["main"]["temp_min"]))
    temp_max = int(round(weather["main"]["temp_max"]))
    formatted = "Today we can expect {0}. The temperature outside is {1} degrees with a low of {2} and a high of {3} degrees.".format(descr, temp, temp_min, temp_max)
    return formatted


def WeatherKelvinToCelsius(weather):
    weather['main']['temp'] -= KELVIN
    weather['main']['temp_min'] -= KELVIN
    weather['main']['temp_max'] -= KELVIN
    weather['wind']['deg'] -= KELVIN


if __name__ == "__main__":
    print RequestWeatherDescription()
# print url
