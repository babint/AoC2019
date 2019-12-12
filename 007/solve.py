#!/usr/bin/env python3

import sys
import copy
from itertools import permutations

sys.path.append("..")
from intcode import IntCode

def load_memory(filename):
	with open(filename) as f:
		data = f.read()
		lines = data.split(',')
	return lines

# Usage Check
if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

# Map argv inputs into variables
script, filename = sys.argv

# Load and Run
memory = load_memory(filename)

# Find the best sequence to maximize thrusters 
best_seq = [-1,0]
for seq in permutations([0,1,2,3,4]):
	signal = 0
	for module in seq:
		signal = IntCode(copy.copy(memory), [module,signal]).process();

	# Better than current max?
	if (int(str(best_seq[1])) < signal):
		best_seq = [seq, signal]


print(f'seq: {best_seq[0]} highest output: {best_seq[1]}')

