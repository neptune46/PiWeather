import led
import temperature
import condition
import time
import RPi.GPIO as GPIO

CODE_SUNNY = 0
CODE_CLOUDY = 1
CODE_PARTLY_CLOUDY = 2
CODE_OVERCAST = 3
CODE_SHOWER_RAIN = 4
CODE_LIGHT_RAIN = 5
CODE_MODERATE_RAIN = 6
CODE_HEAVY_RAIN = 7

def testLED():
    GPIO.setmode(GPIO.BOARD)
    led1 = led.led1 
    led2 = led.led2
    led3 = led.led3
    for i in range(0, 256):
        led1.setByte(i)
        led2.setByte(i)
        led3.setByte(i)
        time.sleep(0.01)
    led1.clear()
    led2.clear()
    led3.clear()

def testCondition():
    condi1 = condition.Condition(0)
    condi2 = condition.Condition(1)
    condi3 = condition.Condition(2)

    condi1.display(CODE_SUNNY)
    time.sleep(1)
    condi2.display(CODE_PARTLY_CLOUDY)
    time.sleep(1)
    condi3.display(CODE_HEAVY_RAIN)
    time.sleep(1)

    condi1.display(CODE_CLOUDY)
    time.sleep(1)
    condi2.display(CODE_OVERCAST)
    time.sleep(1)
    condi3.display(CODE_MODERATE_RAIN)
    time.sleep(1)

    condi1.display(CODE_SHOWER_RAIN)
    time.sleep(1)
    condi2.display(CODE_SHOWER_RAIN)
    time.sleep(1)
    condi3.display(CODE_SUNNY)
    time.sleep(1)
    
    condi1.clear()
    condi2.clear()
    condi3.clear()

def testAirTemp():
    airTemp1 = temperature.tempDisp1
    airTemp2 = temperature.tempDisp2
    airTemp3 = temperature.tempDisp3
    temperature.test(airTemp1)
    temperature.test(airTemp2)
    temperature.test(airTemp3)

def test():
    testLED()
    testAirTemp()
    testCondition()
    
if __name__ == "__main__": 
    try:
        test()
    except KeyboardInterrupt: 
        print "key board interrupt!"
        print "cleanup GPIO ..."
        GPIO.cleanup()
    
    print "cleanup GPIO ..."
    GPIO.cleanup()
    print "exit..."
