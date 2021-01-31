from machine import Pin, Timer

led1 = Pin(16, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led1.value(0)
led2.value(1)
tim = Timer()

def tick(timer):
    global led1, led2
    led1.toggle()
    led2.toggle()

tim.init(freq=2, mode=Timer.PERIODIC, callback=tick)