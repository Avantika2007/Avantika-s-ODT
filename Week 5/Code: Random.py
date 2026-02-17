import random
import time
while True:
  x=random.randint(0,15)
  print(x)
  time.sleep(1)

'''If initilisation does not take place in the while loop, then a random number will be selected and only that will be printed multiple times'''

#-----------------------------------
#Generate random number by pushing a switch
from machine import Pin
import random
import time
s1=Pin(18, Pin.IN, Pin.PULL_UP)
while True:
  s1_value=s1.value()
  if s1_value==0:
    r=random.randint(1,10)
    time.sleep(0.2)
    print(r)
#-----------------------------------
#To generate a random number every second
from machine import Pin
import random
import time
while True:
  r=random.randint(1,10)
  print(r)
  time.sleep(1)
