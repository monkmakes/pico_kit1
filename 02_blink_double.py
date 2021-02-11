from machine import Pin, Timer

led1 = Pin(16, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led1.value(0)
led2.value(1)

def tick(timer):
    led1.toggle()
    led2.toggle()

Timer().init(freq=2, callback=tick)