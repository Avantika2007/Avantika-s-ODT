from machine import Pin
import time #importing time module
led=Pin(2,Pin.OUT)
led.on()
time.sleep(0.2)
led.off()
time.sleep(0.2)
