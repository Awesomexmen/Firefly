import board
import neopixel
import time
from swarm import Swarm
import sched, time
import threading

ORDER = neopixel.GRB
pixel_pin = board.D18
num_pixels = 54

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

swarm = Swarm(6, s)
swarm.begin_flashing(10000, 1, 0.01)

off = (0, 0, 0)
color_id = 0
color_dir = 0
rgb = True

def wheel(pos):
# Input a value 0 to 255 to get a color value.
# The colours are a transition r - g - b - back to r.\
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

def update_leds() -> int:
    global color_id
    global color_dir
    color = wheel(color_id) if rgb else (255,255,102)
    for f in swarm.fireflies:
        intensity = f.get_curr_intensity()
        pixels[mtx_mp[f.coords] + 3] = (int(color[0] * intensity), int(color[1] * intensity), int(color[2] * intensity))
        f.tick()
    pixels.show()
    if color_id < 255 and color_dir == 0:
        color_id += 1
    elif color_id == 255 and color_dir == 0:
        color_dir = 1
        color_id = 254
    elif color_id > 0 and color_dir == 1:
        color_id -= 1
    elif color_id == 0 and color_dir == 1:
        color_dir = 0
        color_id = 1
    
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

set_interval(update_leds, 0.05)
s.run()
