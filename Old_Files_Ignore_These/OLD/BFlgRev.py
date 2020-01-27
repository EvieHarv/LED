import board
import neopixel
import time
import random

PIN = board.D18 # Only 10, 12, 18, 21
PIXEL_NUM = 300
BRIGHTNESS = .5
ORDER = neopixel.GRB # Alt: RGBW/GRBW/(RGB?)

pixels = neopixel.NeoPixel(PIN, PIXEL_NUM, brightness=BRIGHTNESS, auto_write=False, pixel_order=neopixel.GRB)

for x in range(300):
	if (x < 99):
		pixels[x] = (0, 56, 168)
	elif (x < 199):
		pixels[x] = (155, 79, 150)
	else:
		pixels[x] = (175, 2, 112)

pixels.show()