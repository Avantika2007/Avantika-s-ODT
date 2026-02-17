from machine import Pin
import time
s=Pin(14, Pin.IN, Pin.PULL_UP)
led=Pin(23, Pin.OUT)
while True:
  s_value=s.value()
  if s_value==0:
    led.on()
    print('Obstacle Detected')
  else:
    led.off()
