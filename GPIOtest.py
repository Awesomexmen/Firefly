from gpiozero import LED
from time import sleep

leds = [(4, LED(4)), (5, LED(5)), (6, LED(6)), (12, LED(12)), (13, LED(13)), ( 16, LED(16)), (17, LED(17))]

while True:
    for id, led in leds:
        print('Invert ID', id)
        led.toggle()
        sleep(.02)

