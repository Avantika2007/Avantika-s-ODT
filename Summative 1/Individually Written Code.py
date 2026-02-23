from machine import Pin, PWM, TouchPad
import time
#no input given to the cat: 
l1=PWM(12,Pin.OUT)
l2=PWM(14,Pin.OUT)
l3=PWM(27,Pin.OUT)
l1.freq(500)
l2.freq(500)
l3.freq(500)
b=Pin(5, Pin.OUT)

while True:
    #if capacitative touch
    #if reed switch
    #else:
    for i in range(0,256,1):
        l1.duty(i)
        l2.duty(i)
        l3.duty(i)
        time.sleep(0.002)
    for i in range (256,-1,-1):
        l1.duty(i)
        l2.duty(i)
        l3.duty(i)
        time.sleep(0.002)

#Touching tail capacitance and servo motor 

c=TouchPad(Pin(4))
s=PWM(Pin(18), Pin.OUT)
s.freq(50)
while True:
    c_value=c.read()
    print(c_value)
    time.sleep(0.2)
    if c_value <200:
        for i in range (0,120,1):
            s.duty(i)
            time.sleep(0.001)
        for j in range (120, 0, -1):
            s.duty(j)
            time.sleep(0.001)
            l1.duty(512)
            l2.duty(512)
            l3.duty(512)
            time.sleep(0.02)
            l1.duty(0)
            l2.duty(0)
            l3.duty(0)
            time.sleep(0.001)
            
       
            
        

        
            
        
    
