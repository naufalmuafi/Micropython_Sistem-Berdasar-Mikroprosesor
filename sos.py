from machine import Pin
import time

led = Pin(2, Pin.OUT)

while True:  
  for i in range(0, 3):
    led.value(1)
    time.sleep(0.3)
    led.value(0)
    time.sleep(0.3)
  for i in range(0, 3):
    led.value(1)
    time.sleep(2)
    led.value(0)
    time.sleep(0.3)
  for i in range(0, 3):
    led.value(1)
    time.sleep(0.3)
    led.value(0)
    time.sleep(0.3)
  led.value(0)
  time.sleep(3)
