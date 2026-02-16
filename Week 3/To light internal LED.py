#To light internal LED of ESP32
from machine import Pin
led=Pin(2, Pin.OUT) #Pin class is input by default; 2 is port no.
led.on() #switched led on
#--------------------------
#LED with delay
from machine import Pin
import time #importing time module
led=Pin(2,Pin.OUT)
led.on()
time.sleep(0.2)
led.off()
time.sleep(0.2)
