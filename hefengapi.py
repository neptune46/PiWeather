#!/usr/bin/env python
# encoding: utf-8

import urllib2
import json

CODE_SUNNY = 0
CODE_CLOUDY = 1
CODE_PARTLY_CLOUDY = 2
CODE_OVERCAST = 3
CODE_SHOWER_RAIN = 4
CODE_LIGHT_RAIN = 5
CODE_MODERATE_RAIN = 6
CODE_HEAVY_RAIN = 7

codeMap = {
    "100": CODE_SUNNY, #晴	Sunny/Clear	100.png
    "101": CODE_CLOUDY, #多云	Cloudy	101.png
    "102": CODE_CLOUDY, #少云	Few Clouds	102.png
    "103": CODE_PARTLY_CLOUDY, #晴间多云	Partly Cloudy	103.png
    "104": CODE_OVERCAST, #阴	Overcast	104.png
    "200": CODE_SUNNY, #有风	Windy	200.png
    "201": CODE_SUNNY, #平静	Calm	201.png
    "202": CODE_SUNNY, #微风	Light Breeze	202.png
    "203": CODE_SUNNY, #和风	Moderate/Gentle Breeze	203.png
    "204": CODE_SUNNY, #清风	Fresh Breeze	204.png
    "205": CODE_CLOUDY, #强风/劲风	Strong Breeze	205.png
    "206": CODE_CLOUDY, #疾风	High Wind, Near Gale	206.png
    "207": CODE_CLOUDY, #大风	Gale	207.png
    "208": CODE_CLOUDY, #烈风	Strong Gale	208.png
    "209": CODE_OVERCAST, #风暴	Storm	209.png
    "210": CODE_OVERCAST, #狂爆风	Violent Storm	210.png
    "211": CODE_OVERCAST, #飓风	Hurricane	211.png
    "212": CODE_OVERCAST, #龙卷风	Tornado	212.png
    "213": CODE_OVERCAST, #热带风暴	Tropical Storm	213.png
    "300": CODE_SHOWER_RAIN, #阵雨	Shower Rain	300.png
    "301": CODE_HEAVY_RAIN, #强阵雨	Heavy Shower Rain	301.png
    "302": CODE_SHOWER_RAIN, #雷阵雨	Thundershower	302.png
    "303": CODE_SHOWER_RAIN, #强雷阵雨	Heavy Thunderstorm	303.png
    "304": CODE_SHOWER_RAIN, #雷阵雨伴有冰雹	Hail	304.png
    "305": CODE_LIGHT_RAIN, #小雨	Light Rain	305.png
    "306": CODE_MODERATE_RAIN, #中雨	Moderate Rain	306.png
    "307": CODE_HEAVY_RAIN, #大雨	Heavy Rain	307.png
    "308": CODE_HEAVY_RAIN, #极端降雨	Extreme Rain	308.png
    "309": CODE_LIGHT_RAIN, #毛毛雨/细雨	Drizzle Rain	309.png
    "310": CODE_HEAVY_RAIN, #暴雨	Storm	310.png
    "311": CODE_HEAVY_RAIN, #大暴雨	Heavy Storm	311.png
    "312": CODE_HEAVY_RAIN, #特大暴雨	Severe Storm	312.png
    "313": CODE_MODERATE_RAIN, #冻雨	Freezing Rain	313.png
    "400": CODE_LIGHT_RAIN, #小雪	Light Snow	400.png
    "401": CODE_MODERATE_RAIN, #中雪	Moderate Snow	401.png
    "402": CODE_HEAVY_RAIN, #大雪	Heavy Snow	402.png
    "403": CODE_HEAVY_RAIN, #暴雪	Snowstorm	403.png
    "404": CODE_MODERATE_RAIN, #雨夹雪	Sleet	404.png
    "405": CODE_MODERATE_RAIN, #雨雪天气	Rain And Snow	405.png
    "406": CODE_SHOWER_RAIN, #阵雨夹雪	Shower Snow	406.png
    "407": CODE_SHOWER_RAIN, #阵雪	Snow Flurry	407.png
    "500": CODE_CLOUDY, #薄雾	Mist	500.png
    "501": CODE_OVERCAST, #雾	Foggy	501.png
    "502": CODE_CLOUDY, #霾	Haze	502.png
    "503": CODE_CLOUDY, #扬沙	Sand	503.png
    "504": CODE_CLOUDY, #浮尘	Dust	504.png
    "507": CODE_OVERCAST, #沙尘暴	Duststorm	507.png
    "508": CODE_OVERCAST, #强沙尘暴	Sandstorm	508.png
    "900": CODE_SUNNY, #热	Hot	900.png
    "901": CODE_OVERCAST, #冷	Cold	901.png
    "999": CODE_CLOUDY #未知	Unknown	999.png
}

def getWeather():
    data = []
    response = urllib2.urlopen('https://free-api.heweather.com/v5/forecast?city=shanghai&lang=en&key=0ea65b86e2a94335a1bbdb09017eb470')
    weather = response.read()
    dataJSON = json.loads(weather)

    day1 = [
        codeMap[dataJSON["HeWeather5"][0]["daily_forecast"][0]["cond"]["code_n"]],
        int(dataJSON["HeWeather5"][0]["daily_forecast"][0]["tmp"]["min"]),
        int(dataJSON["HeWeather5"][0]["daily_forecast"][0]["tmp"]["max"]),
    ]

    day2 = [
        codeMap[dataJSON["HeWeather5"][0]["daily_forecast"][1]["cond"]["code_n"]],
        int(dataJSON["HeWeather5"][0]["daily_forecast"][1]["tmp"]["min"]),
        int(dataJSON["HeWeather5"][0]["daily_forecast"][1]["tmp"]["max"])
    ]

    day3 = [
        codeMap[dataJSON["HeWeather5"][0]["daily_forecast"][2]["cond"]["code_n"]],
        int(dataJSON["HeWeather5"][0]["daily_forecast"][2]["tmp"]["min"]),
        int(dataJSON["HeWeather5"][0]["daily_forecast"][2]["tmp"]["max"])
    ]

    data = [day1, day2, day3]

    return data
