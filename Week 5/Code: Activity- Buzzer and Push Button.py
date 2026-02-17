from machine import Pin
import time
s=Pin(18, Pin.IN, Pin.PULL_UP)
b=Pin(14, Pin.OUT)
while True:
  s_value=s.value()
  print('ok')
  time.sleep(0.2)
  if s_value==0: #push button is on
    b.on()
    time.sleep(0.23)
    b.off()
    time.sleep(0.23)
    print ('yay') 
