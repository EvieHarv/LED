#color,color,int_bound_1_300

import board
import neopixel
import time
import random

def run(pixels, stop, var):
	split = var.split(',')
	print(split)
	for x in range(0,299):
		if x<int(split[6]):
			pixels[x] = ((int(split[0]), int(split[1]), int(split[2])))
		else:
			pixels[x] = ((int(split[3]), int(split[4]), int(split[5])))
	pixels.show()
