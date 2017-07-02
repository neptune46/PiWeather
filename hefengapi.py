import urllib2
import json

response = urllib2.urlopen('https://free-api.heweather.com/v5/forecast?city=shanghai&lang=en&key=0ea65b86e2a94335a1bbdb09017eb470')
weather = response.read()
dataJSON = json.loads(weather)

print "day1: "
print dataJSON["HeWeather5"][0]["daily_forecast"][0]["cond"]["code_n"]
print dataJSON["HeWeather5"][0]["daily_forecast"][0]["tmp"]["max"]
print dataJSON["HeWeather5"][0]["daily_forecast"][0]["tmp"]["min"]

print "day2: "
print dataJSON["HeWeather5"][0]["daily_forecast"][1]["cond"]["code_n"]
print dataJSON["HeWeather5"][0]["daily_forecast"][1]["tmp"]["max"]
print dataJSON["HeWeather5"][0]["daily_forecast"][1]["tmp"]["min"]

print "day3: "
print dataJSON["HeWeather5"][0]["daily_forecast"][2]["cond"]["code_n"]
print dataJSON["HeWeather5"][0]["daily_forecast"][2]["tmp"]["max"]
print dataJSON["HeWeather5"][0]["daily_forecast"][2]["tmp"]["min"]