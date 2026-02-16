from machine import Pin
import time
LED=Pin(2,PIn.OUT)
while (n>3):
  LED.on()
  time.sleep(0.2)
  LED.off()
  time.sleep(0.2)

#alternatively
from machine import Pin
import time
LED=Pin(2,PIn.OUT)
while True:
  LED.on()
  time.sleep(0.2)
  LED.off()
  time.sleep(0.2)

#--------------------------------
#To run a specific number of times with While Loop
from machine import Pin
import time
l=Pin(2, Pin.OUT)
n=6
while True:
  led.on()
  time.sleep(0.2)
  led.off()
  time.sleep(0.2)
  n-=1

#OUTPUT: LED blinks three times
