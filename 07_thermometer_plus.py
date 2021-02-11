from machine import Pin, PWM, ADC, Timer
from utime import sleep

set_temp = 25

buzzerA = Pin(15, Pin.OUT)
buzzerA.high()
buzzerB = Pin(14, Pin.OUT)
buzzerB.low()
buzz = False

servo = PWM(Pin(16))
servo.freq(50) # pulse every 20ms

temp_sensor = ADC(4)
points_per_volt = 3.3 / 65535

def tick(timer):
    if buzz:
        buzzerA.toggle()
        buzzerB.toggle()

def read_temp_c():
    reading = temp_sensor.read_u16() * points_per_volt
    temp_c = 27 - (reading - 0.706)/0.001721
    return temp_c

def set_angle(angle, min_pulse_us=500, max_pulse_us=2500):
    us_per_degree = (max_pulse_us - min_pulse_us) / 180
    pulse_us = us_per_degree * angle + min_pulse_us
    # duty 0 to 1023. At 50Hz, each duty_point is 20000/65535 = 0.305 µs/duty_point
    duty = int(pulse_us / 0.305)
    #print("angle=" + str(angle) + " pulse_us=" + str(pulse_us) + " duty=" + str(duty))
    servo.duty_u16(duty)
    
angle = 90
set_angle(90)
min_angle = 10
max_angle = 170
min_temp = 0
max_temp = 50
angle_per_degree_c = (max_angle - min_angle) / (max_temp - min_temp)

Timer().init(freq=1200, callback=tick)

while True:
    temp_c = read_temp_c()
    angle = min_angle + (temp_c - min_temp) * angle_per_degree_c
    if angle >= min_angle and angle <= max_angle:
        set_angle(180-angle)
    buzz = (temp_c > set_temp)
    print(temp_c)
    sleep(0.5)

