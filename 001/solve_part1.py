#!/usr/bin/env python3

import sys
import math

if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

fuel = 0
with open(sys.argv[1]) as f:
	data = f.read()
	lines = data.splitlines()

	for mass in lines:
		# floor(m/3) - 2
		fuel = fuel + (math.floor(int(mass)/3) - 2)

print(f'fuel needed: {fuel}')
print("\ndone.");