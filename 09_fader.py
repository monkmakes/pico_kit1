from machine import Pin, ADC, PWM
from utime import sleep

blue_ch = PWM(Pin(15))
pot = ADC(28)

while True:
    reading = pot.read_u16()
    sleep(0.1) # recovery time for ADC
    print(reading)
    blue_ch.duty_u16(reading)
