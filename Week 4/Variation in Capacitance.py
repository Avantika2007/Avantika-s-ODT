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

#------------------------------------

from machine import Pin, TouchPad
import time
l1=Pin(12,Pin.OUT)
l2=Pin(12,Pin.OUT)
t=TouchPad(Pin(4))
while True:
  t_value=t.read()
  time.sleep(0.2)
  if t_value < 300:
    print('Pin 4 is touched')
    l1.on()
    time.sleep(0.2)
    l1.off()
    time.sleep(0.2)
  else:
    print('Not touched')
    l2.on()
    time.sleep(0.2)
    l2.off()
    time.sleep(0.2)

'''OUTPUT: When the jumper wire is not touched, l2 switches on, and 'not touched' is printed
When the jumper wire is touched, values go below 300, l1 is swtiched on and 'Pin 4 is touched' is printed'''
