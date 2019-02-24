import board
import neopixel
import time

ORDER = neopixel.GRB
pixel_pin = board.D18
num_pixels = 30

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.03, auto_write=False, pixel_order=ORDER)
meta_pixels = [[0, 0, 0, 0] for _ in range(len(pixels))]

up_to = 0

for up_to in range(len(pixels)):
    for _ in range(255):
        for bulb in range(up_to):
            stage = meta_pixels[bulb][3]
            if stage < 255:
                meta_pixels[bulb][0] += 1
            elif stage < 255 * 2:
                meta_pixels[bulb][0] -= 1
            elif stage < 255 * 3:
                meta_pixels[bulb][1] += 1
            elif stage < 255 * 4:
                meta_pixels[bulb][1] -= 1
            elif stage < 255 * 5:
                meta_pixels[bulb][2] += 1
            elif stage < 255 * 6:
                meta_pixels[bulb][2] -= 1
            else:
                meta_pixels[bulb] = [0,0,0,0]
                continue
            pixels[bulb] = (meta_pixels[bulb][0], meta_pixels[bulb][1], meta_pixels[bulb][2])
            meta_pixels[bulb][3] += 1
        pixels.show()

