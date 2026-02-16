#To obtain value
from machine import Pin
s=Pin(4, Pin.IN, Pin.PULL_UP)
s_value= s.value()
print(s_value)

#To obtain continuous values
from machine import Pin
import time
s=Pin(4, Pin.IN, Pin.PULL_UP)
while True:
  s_value= s.value()
  print(s_value)
  time.sleep(0.2)
