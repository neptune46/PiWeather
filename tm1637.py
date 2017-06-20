import RPi.GPIO as GPIO
import time

CLK = 11
DIO = 12

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DIO, GPIO.OUT)

def delay_ms():
    time.sleep(0.001)
    
def i2c_start():
    GPIO.output(CLK, GPIO.HIGH)
    GPIO.output(DIO, GPIO.HIGH)
    delay_ms()
    GPIO.output(DIO, GPIO.LOW)
    delay_ms()
    
def i2c_stop():
    GPIO.output(CLK, GPIO.LOW)
    delay_ms()
    GPIO.output(DIO, GPIO.LOW)
    delay_ms()
    GPIO.output(CLK, GPIO.HIGH)
    delay_ms()
    GPIO.output(DIO, GPIO.HIGH)
    delay_ms()

def i2c_ask():
    GPIO.output(CLK, GPIO.LOW)
    delay_ms()
    
    # set data pin as input
    GPIO.setup(DIO, GPIO.IN)
    delay_ms()
    
    count = 10
    
    # read ack signal
    while GPIO.input(DIO) and count:
        delay_ms()
        print count
        count = count - 1
    
    GPIO.output(CLK, GPIO.HIGH)
    delay_ms()
    GPIO.output(CLK, GPIO.LOW)
    delay_ms()
    
    # set data pin as output
    GPIO.setup(DIO, GPIO.OUT)
    delay_ms()
    
def i2c_write_byte(data):
    for i in range(8):
        GPIO.output(CLK, GPIO.LOW)
        delay_ms()
        if data & 0x01:
            GPIO.output(DIO, GPIO.HIGH)
        else:
            GPIO.output(DIO, GPIO.LOW)
        delay_ms()
        data >>= 1
        GPIO.output(CLK, GPIO.HIGH)
        delay_ms()
        
def led8_display(value):
    i2c_start()
    i2c_write_byte(0x40) # 0x40 - auto address ; 0x44 - fixed address
    i2c_ask()
    i2c_stop()
    
    i2c_start()
    i2c_write_byte(0xc0) # set start address
    i2c_ask()
    for i in range(4):
        i2c_write_byte(value)
        i2c_ask()
    i2c_stop()
    
    i2c_start()
    i2c_write_byte(0x88) # set maxium brightness
    i2c_ask()
    time.sleep(1)
    i2c_stop()

def main():
    led8_display(0x7f)
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