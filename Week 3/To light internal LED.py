#To light internal LED of ESP32
from machine import Pin
led=Pin(2, Pin.OUT) #Pin class is input by default; 2 is port no.
led.on() #switched led on
