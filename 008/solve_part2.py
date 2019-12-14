#!/usr/bin/env python3

import sys
from math import floor
from enum import IntEnum

class COLORS(IntEnum):
		BLACK = 0,
		WHITE = 1,
		TRANS = 2

def buildLayers(width, height, data):
	layers = []
	pixels = width * height
	layer_count = floor(len(data) / pixels)

	for layer in range(0, layer_count):
		start = layer*pixels
		end = (layer*pixels)+pixels
		layers.insert(layer, data[start:end])

	return layers

def displayImage(image, width):
	for i,pixel in enumerate(image):
		if (i%width==0): print("")
		if (pixel == COLORS.BLACK):
			print(" ", end =" ")
		elif (pixel == COLORS.WHITE):
			print("#", end =" ")
	print()


def read_file(filename):
	with open(filename) as f:
		data = f.readline()
		nums = [int(i) for i in data]
	return nums

# Usage Check
if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

# -------------------
# MAIN PROGRAM
# -------------------

# Map argv inputs into variables
script, filename = sys.argv

# load File
data = read_file(filename)

# setup
width = 25
height = 6
image =  [COLORS.TRANS for s in range(width*height)] # full transparent image
layers = buildLayers(width,height,data)

# Replace any pixel in image with layer's non-trans pixel
layers.reverse()
for i,layer in enumerate(layers):
	for j,pixel in enumerate(image):
		if (layer[j] != COLORS.TRANS): image[j] = layer[j] 


displayImage(image, width)
