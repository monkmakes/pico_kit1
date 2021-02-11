from machine import Pin, ADC
from utime import sleep

red_ch = Pin(16, Pin.OUT)
green_ch = Pin(17, Pin.OUT)
pot = ADC(28)
subject = ADC(27)

while True:
    threshold = pot.read_u16()
    sleep(0.1) # recovery time for ADC
    gsr = subject.read_u16()
    sleep(0.1) # recovery time for ADC
    print("threshold=" + str(threshold) + " gsr=" + str(gsr))
    if gsr > threshold:
        red_ch.high()
        green_ch.low()
    else:
        red_ch.low()
        green_ch.high()
