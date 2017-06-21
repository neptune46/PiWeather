import tm1637
import time
import RPi.GPIO as GPIO

CLK = 11
DIO = 12

def main():
    led = tm1637.TM1637(CLK, DIO)
    led.display_digit(['0', '1', '2', '3'])
    led.display_digit(['4', '5', '6', '7'])
    led.display_digit(['8', '9', 'A', 'B'])
    led.display_digit(['C', 'D', 'E', 'F'])
    led.display_digit(['-', '-', '-', '-'])
    print "press any key to exit...wait for 2 seconds"
    #r = raw_input()
    time.sleep(1)
    
if __name__ == "__main__": 
    try:
        main()
    except KeyboardInterrupt: 
        print "key board interrupt!"
        #GPIO.cleanup()
        
    print "exit..."
    GPIO.cleanup()
