from machine import Pin, ADC, Timer
from utime import sleep_us, sleep, ticks_us

blue_ch = Pin(15, Pin.OUT)
pot = ADC(28)

ms_count = 0
period = 0

def tick(timer):
    global ms_count
    ms_count += 1
    if ms_count > period:
        blue_ch.toggle()
        ms_count = 0

tim = Timer()
tim.init(freq=2000, callback=tick)

old_reading = 0

while True:
    reading = int(pot.read_u16() / 256) # 0 to 255
    sleep(0.1) # recovery time
    if reading != old_reading:
        frequency = int(reading) 
        if frequency < 1:
            frequency = 1
        print(frequency)
        period = int(1000 / frequency)
        old_reading = reading
    
    


