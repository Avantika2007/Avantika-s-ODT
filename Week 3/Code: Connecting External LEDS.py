from machine import Pin
import time
led=Pin(12, Pin.OUT)
while True:
  led.on()
  time.sleep(0.2)
  led.off()
  time.sleep(0.2)

#Multiple External LEDs
from machine import Pin
import time
l1=Pin(12,Pin.OUT)
l2=Pin(14, Pin.OUT)
while True:
  l1.on()
  time.sleep(0.1)
  l1.off()
  time.sleep(0.1)
  l1.on()
  time.sleep(0.25)
  l1.off()
  time.sleep(0.25)
  l2.on()
  time.sleep(0.25)
  l2.off()
  time.sleep(0.25)
  l2.on()
  time.sleep(0.1)
  l2.off()
  time.sleep(0.1)
  
  
