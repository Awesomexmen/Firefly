import board
import neopixel
import time

ORDER = neopixel.GRB
pixel_pin = board.D18
num_pixels = 30

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



