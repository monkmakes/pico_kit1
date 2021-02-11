from machine import ADC, PWM, Pin
from utime import sleep
from math import sqrt

servo = PWM(Pin(16))
servo.freq(50) # pulse every 20ms

light_sensor = ADC(28)
dark_reading = 200
scale_factor = 2.5

def set_angle(angle, min_pulse_us=500, max_pulse_us=2500):
    us_per_degree = (max_pulse_us - min_pulse_us) / 180
    pulse_us = us_per_degree * angle + min_pulse_us
    # duty 0 to 1023. At 50Hz, each duty_point is 20000/65535 = 0.305 µs/duty_point
    duty = int(pulse_us / 0.305)
    #print("angle=" + str(angle) + " pulse_us=" + str(pulse_us) + " duty=" + str(duty))
    servo.duty_u16(duty)

def read_light():
    reading = light_sensor.read_u16()
    # print(reading)
    percent = int(sqrt(reading - dark_reading) / scale_factor)
    if percent < 0:
        percent = 0
    elif percent > 100:
        percent = 100
    return (percent)

min_angle = 10
max_angle = 160
min_light = 0
max_light = 100
angle_per_percent = (max_angle - min_angle) / (max_light - min_light)

while True:
    light_level = read_light()
    print(light_level)
    angle = min_angle + (light_level - min_light) * angle_per_percent
    set_angle(max_angle - angle)
    sleep(0.2)