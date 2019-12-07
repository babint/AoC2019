#!/usr/bin/env python3

import sys
import math

def calc_fuel(mass):
	# calculate fuel needed for this mass
	fuel = (math.floor(int(mass)/3) - 2)

	# calc fuel needed to haul this fuel around
	if (fuel > 7): fuel = fuel + calc_fuel(fuel)

	return fuel

if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

fuel = 0
with open(sys.argv[1]) as f:
	data = f.read()
	lines = data.splitlines()

	for mass in lines:
		# floor(m/3) - 2
		fuel = fuel + calc_fuel(mass)

print(f'fuel needed: {fuel}')
print("\ndone.");
