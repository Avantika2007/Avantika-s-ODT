#to light up neopixel LEDS
from machine import Pin
import time
import neopixel
while True:
  x=neopixel.NeoPixel(Pin(12),16) #16 is number of LEDs on the neopixel
  x[0]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[1]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[2]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[3]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[4]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[5]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[6]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[7]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[8]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[9]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[10]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[11]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[12]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[13]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[14]=(255,0,255) #purple colour
  time.sleep(0.2)
  x[15]=(255,0,255) #purple colour
  time.sleep(0.2)
  x.write()

#OR, using for loop:
from machine import Pin
import time
import neopixel
x=neopixel.NeoPixel(Pin(12),16)
while True:
  for i in range(0,16,1):
    print(i)
    x[i]=(255,0,255)
    time.sleep(0.2)
    x.write()

#-------------------------



