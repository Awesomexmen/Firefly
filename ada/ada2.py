import board
import neopixel
import time
from swarm import Swarm
import sched, time
import threading

ORDER = neopixel.GRB
pixel_pin = board.D18
num_pixels = 50

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.03, auto_write=False, pixel_order=ORDER)

mtx_mp = {
    (0,0): 0,
    (0,1): 1,
    (0,2): 2,
    (0,3): 3,
    (0,4): 4,
    (0,5): 5,
    (1,5): 9,
    (1,4): 10,
    (1,3): 11,
    (1,2): 12,
    (1,1): 13,
    (1,0): 14,
    (2,0): 18,
    (2,1): 19,
    (2,2): 20,
    (2,3): 21,
    (2,4): 22,
    (2,5): 23,
    (3,5): 27,
    (3,4): 28,
    (3,3): 29,
    (3,2): 30,
    (3,1): 31,
    (3,0): 32,
    (4,0): 36,
    (4,1): 37,
    (4,2): 38,
    (4,3): 39,
    (4,4): 40,
    (4,5): 41,
    (5,5): 45,
    (5,4): 46,
    (5,3): 47,
    (5,2): 48,
    (5,1): 49,
    (5,0): 50
}

s = sched.scheduler(time.time, time.sleep)

swarm = Swarm(18, s)
swarm.begin_flashing(60, 1, 0.01)

color = (255, 0, 0)
off = (0, 0, 0)

def update_leds:
    for f in swarm.fireflies:
        if f.flashing:
            pixels[mtx_mp[f.coords]] = color
        else:
            pixel[mtx_mp[f.coords]] = off

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

set_interval(update_leds, 0.05)
s.run()
