from machine import Pin, ADC, PWM
from time import sleep

led_pwm = PWM(Pin(5), 5000)
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT)

while True:
    pot_value = pot.read()
    print(pot_value)
    led_pwm.duty(pot_value)
    sleep(0.1)