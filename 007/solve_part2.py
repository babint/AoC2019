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

# Go through all permutations of settings
best_seq = [-1,0]
for phase_settings in permutations([5,6,7,8,9]):
	#Setup new Amps with their own memory
	amplifiers = [
	    IntCode(copy.copy(memory), phase_settings[0]),
	    IntCode(copy.copy(memory), phase_settings[1]),
	    IntCode(copy.copy(memory), phase_settings[2]),
	    IntCode(copy.copy(memory), phase_settings[3]),
	    IntCode(copy.copy(memory), phase_settings[4]),
	]

	#Determine Siginal for these settings
	signal = 0
	i = 0
	while (True):
		# Setup
		i = (i % len(amplifiers))
		amp = amplifiers[i]	
		setting = phase_settings[i]
		amp.inputs.append(signal)

		if (amp.state == IntCode.STATES.ENDED): break
		
		signal = amp.process()	
		i+=1

	# Better than current max?
	if (int(str(best_seq[1])) < signal):
		best_seq = [phase_settings, signal]

print(f'seq: {best_seq[0]} highest signal: {best_seq[1]}')

