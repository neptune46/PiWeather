import led
import temperature
import condition
import time
import RPi.GPIO as GPIO


def main():
    print "start..."
    time.sleep(10)
    
if __name__ == "__main__": 
    try:
        main()
    except KeyboardInterrupt: 
        print "key board interrupt!"
    
    print "cleanup GPIO in exit..."
    GPIO.cleanup()
    print "exit..."
