from machine import Pin
import time
l=PWM(Pin(4))
l.freq(1000) #PWM signal completes 1000 on and off cycles every second; higher frequencies avoid flickering in LEDs
while True:
  for i in range (0,1024,1):
    l.duty(i)
    time.sleep(0.2)
  for j in range (1023, 1, -1):
    l.duty(j)
    time.sleep(0.2) 
