import led
import temperature
import time
import RPi.GPIO as GPIO

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

def testAirTemp():
    airTemp1 = temperature.tempDisp1
    airTemp2 = temperature.tempDisp2
    airTemp3 = temperature.tempDisp3
    temperature.test(airTemp1)
    temperature.test(airTemp2)
    temperature.test(airTemp3)

def main():
    testLED()
    testAirTemp()
    
if __name__ == "__main__": 
    try:
        main()
    except KeyboardInterrupt: 
        print "key board interrupt!"
        print "cleanup GPIO ..."
        GPIO.cleanup()
    
    print "cleanup GPIO ..."
    GPIO.cleanup()
    print "exit..."
