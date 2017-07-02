import urllib2
import json

def getWeather():
    data = []
    response = urllib2.urlopen('https://free-api.heweather.com/v5/forecast?city=shanghai&lang=en&key=0ea65b86e2a94335a1bbdb09017eb470')
    weather = response.read()
    dataJSON = json.loads(weather)

    day1 = [
        4, # dataJSON["HeWeather5"][0]["daily_forecast"][0]["cond"]["code_n"],
        int(dataJSON["HeWeather5"][0]["daily_forecast"][0]["tmp"]["min"]),
        int(dataJSON["HeWeather5"][0]["daily_forecast"][0]["tmp"]["max"]),
    ]

    day2 = [
        3, #dataJSON["HeWeather5"][0]["daily_forecast"][1]["cond"]["code_n"],
        int(dataJSON["HeWeather5"][0]["daily_forecast"][1]["tmp"]["min"]),
        int(dataJSON["HeWeather5"][0]["daily_forecast"][1]["tmp"]["max"])
    ]

    day3 = [
        5, #dataJSON["HeWeather5"][0]["daily_forecast"][2]["cond"]["code_n"],
        int(dataJSON["HeWeather5"][0]["daily_forecast"][2]["tmp"]["min"]),
        int(dataJSON["HeWeather5"][0]["daily_forecast"][2]["tmp"]["max"])
    ]

    data = [day1, day2, day3]

    return data
