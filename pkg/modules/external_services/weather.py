from pkg.utilservices import utility

baseUrl = 'http://api.openweathermap.org/data/2.5/weather'
apiKey = utility.OpenJson('pkg/keys/weatherAPIKey.json')['key']
city = 'Sydney'
url = baseUrl + '?q=' + city + "&APPID=" + apiKey
KELVIN = 273.15


class Weather():
    def __init__(self):
        pass

    def OnRequest(self, requestBody):
        return self.RequestWeather()

    def RequestWeather(self):
        weatherData = utility.GetJson(url)
        self.WeatherKelvinToCelsius(weatherData)
        return weatherData

    def RequestWeatherDescription(self):
        weather = self.RequestWeather()
        descr = weather["weather"][0]['description']
        temp = int(round(weather["main"]["temp"]))
        # temp_min = int(round(weather["main"]["temp_min"])) THIS SEEMS TO BE AREA MIN NOT DAY MIN
        # temp_max = int(round(weather["main"]["temp_max"]))
        formatted = "Today we can expect {0}. The temperature outside is {1} degrees.".format(descr, temp)
        return formatted

    def WeatherKelvinToCelsius(self, weather):
        weather['main']['temp'] -= KELVIN
        weather['main']['temp_min'] -= KELVIN
        weather['main']['temp_max'] -= KELVIN
        weather['wind']['deg'] -= KELVIN


# if __name__ == "__main__":
#     print RequestWeatherDescription()
# print url
