from machine import Pin,PWM, TouchPad
import time
c=TouchPad(Pin(4))
r=Pin(32,Pin.IN,Pin.PULL_UP)
l1=PWM(Pin(12,Pin.OUT))
l2=PWM(Pin(14,Pin.OUT))
l3=PWM(Pin(27,Pin.OUT))
b=PWM(Pin(5,Pin.OUT))
s=PWM(Pin(18), Pin.OUT)
l1.freq(500)
l2.freq(500)
l3.freq(500)
s.freq(50)

#ANGRY TAIL
while True:
    c_value=c.read()
    print(c_value)
    time.sleep(0.2)
    r_val=r.value()
    print(r_val)
    time.sleep(0.2)
    if c_value <200:
        for i in range(900,1400,1):    #buzzer
            b.freq(i)
            b.duty(600)
            time.sleep(0.001)
        for i in range(1400,1100,-1):
            b.freq(i)
            b.duty(512)
            time.sleep(0.001)
        for i in range(1100,1600,1):
            b.freq(i)
            b.duty(600)
            time.sleep(0.001)
        for i in range(1600,1200,-1):
            b.freq(i)
            b.duty(512)
            time.sleep(0.001)
        for i in range (0,80,1):      #motor
            s.duty(i)
            time.sleep(0.001)
        for j in range (80, 0, -1):
            s.duty(j)
            time.sleep(0.001)
            l1.duty(512)               #LEDs
            l2.duty(512)
            l3.duty(512)
            time.sleep(0.02)
            l1.duty(0)
            l2.duty(0)
            l3.duty(0)
            time.sleep(0.001)
            print('1')

#HAPPY FISH
    if r_val==0:
       l1.duty(1023)
       l2.duty(1023)
       l3.duty(1023)
       time.sleep(0.05)
       l1.duty(0)
       l2.duty(0)
       l3.duty(0)
       time.sleep(0.05)
       b.duty(512)
       for x in range(2000,2100,1):
           b.freq(x)
           time.sleep(0.001)

#DEFAULT [No Switch]
    else:
        b.duty(0)
        for i in range(0,256,1):
            l1.duty(i)
            l2.duty(i)
            l3.duty(i)
            print("l2")
            time.sleep(0.002)
            
        for i in range (256,-1,-1):
            l1.duty(i)
            l2.duty(i)
            l3.duty(i)
            print("l1")
            time.sleep(0.002)
    time.sleep(0.01)
      


    
   




        
        
    


