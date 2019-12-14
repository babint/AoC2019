#!/usr/bin/env python3

import sys
from math import floor

def read_file(filename):
	with open(filename) as f:
		data = f.readline()
		nums = list(data)
	return nums

# Usage Check
if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

# Map argv inputs into variables
script, filename = sys.argv

# Load and Run
data = read_file(filename)

width = 25
height = 6
pixels = width * height
layer_count = floor(len(data) / pixels)
min_layer = [sys.maxsize, -1, []] # [num0, layer_num, layer_data]

for layer in range(0, layer_count):
	start = layer*pixels
	end = (layer*pixels)+pixels
	layer_data = data[start:end]
	zero_count = sum(1 for i in layer_data if int(i) != 0) 

	# Check layer with min number of 0's it in
	if (zero_count < min_layer[0]):
		min_layer = [zero_count, layer, layer_data]

# Count the number of 1's and 2's
ones = ''.join('1' if n == '1' else '' for n in min_layer[2])
twos = ''.join('2' if n == '2' else '' for n in min_layer[2])
print(len(ones) * len(twos))
