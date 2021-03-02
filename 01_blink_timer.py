from machine import Pin, Timer

led = Pin(16, Pin.OUT)

def tick(timer):
    led.toggle()

Timer().init(freq=2, callback=tick) # call tick twice a sec