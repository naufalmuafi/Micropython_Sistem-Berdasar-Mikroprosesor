from machine import Pin, PWM
from time import sleep

frequency = 10000
led = PWM(Pin(5), frequency)

while True:
    for duty_cycle in range(0, 500):
        led.duty(duty_cycle)
        sleep(0.005)

