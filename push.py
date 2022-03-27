from machine import Pin
from time import sleep

led = Pin(5, Pin.OUT)
push = Pin(4, Pin.IN)

while True:    
    if (push.value() == 0):
        led.value(0)
    elif (push.value() == 1):
        led.value(1)
        sleep(1)
    #led.value(push.value())
    #sleep(1)