#!/usr/bin/env python
# encoding: utf-8

import temperature
import condition
import hefengapi
import test
import time
import threading
import RPi.GPIO as GPIO

class Weather:
    __weatherCondi = [0, 0, 0]
    __airTemp = [0, 0, 0]

    def __init__(self):
        for i in range(3):
            self.__weatherCondi[i] = condition.Condition(i)
            self.__airTemp[i] = temperature.TempDisplay(i)

    def update(self, data):
        for i in range(3):
            self.__weatherCondi[i].display(data[i][0])
            self.__airTemp[i].setTemp(data[i][1], data[i][2])
    
    def clear(self):
        for i in range(3):
            self.__weatherCondi[i].clear()
            self.__airTemp[i].clear()

wth = Weather()
#wth.update()

def timer_start(n):
    t = threading.Timer(n, refresh, ("",))
    t.start()

def refresh(msg):
    print "refresh..."
    wth.clear()
    test.testAll()
    data = hefengapi.getWeather()
    wth.update(data)
    timer_start(3600)

def main():
    print "start..."
    test.testAll()
    timer_start(1)
    while True:
        time.sleep(10)
    
if __name__ == "__main__": 
    try:
        main()
    except KeyboardInterrupt: 
        print "key board interrupt!"
    
    wth.clear()
    print "cleanup GPIO in exit..."
    GPIO.cleanup()
    print "exit..."
