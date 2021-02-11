from machine import Pin
from utime import sleep, ticks_us

red_ch = Pin(16, Pin.OUT)
green_ch = Pin(17, Pin.OUT)

out_pin = Pin(8, Pin.OUT)
in_pin = Pin(14, Pin.IN)

sense_threshold = 100


def cap_sense_value():
    total = 0
    for i in range(20):
        out_pin.high()
        t0 = ticks_us()
        while in_pin.value() == 0:
            pass
        t1 = ticks_us()
        t = t1 - t0
        out_pin.low()
        sleep(0.01) # allow plenty of time for in_pin to go to 0V
        total += t
    return total / 20

while True:
    value = cap_sense_value()
    print(value)
    if value >= sense_threshold:
        red_ch.low()
        green_ch.high()
    else:
        red_ch.high()
        green_ch.low()
