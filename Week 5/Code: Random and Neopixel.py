#To light up a random LED
from machine import Pin
import time
import neopixel
import random
x=neopixel.NeoPixel(Pin(12),16)
while True:
  r=random.randint(1,16)
  time.sleep(1)
  print(r)
  x[5]=(255,0,255)
  time.sleep(0.2)
  x.write()

#-------------------------
