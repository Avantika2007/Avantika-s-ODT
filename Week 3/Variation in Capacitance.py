from machine import Pin, TouchPad #touchpad is input by default
import time
t=TouchPad(Pin(4))
l=Pin(2, Pin.OUT)
while True:
  t_value=touch.read()
  print(t_value)
  time.sleep(0.4)
  if touch_value<100: 
    l.on()
    time.sleep(0.25)
    l.off()
    time.sleep(0.25)

'''OUTPUT:
When not touching the jumper wire connected to GPIO4, the value is usually higher than 400 and LED does not switch on
When touching the jumper wire, value is lesser than 100, therefore LED swtiches on'''
