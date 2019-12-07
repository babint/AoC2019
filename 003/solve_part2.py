#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

intersections = []
seen = {}
shortest = sys.maxsize
wire_steps = []
with open(sys.argv[1]) as f:
	# Read File split into lines
	lines = f.read().splitlines()		
	for wire, data in enumerate(lines):	
		row = col = steps = 0
		wire_steps.append(wire)
		wire_steps[wire] = {}
		directions = data.split(",") 

		print(f'Drawing wire: {wire}')
		
		# For each direction plot our points
		for direction in directions:
			amount = int(direction[1:len(direction)])
			start_row = row
			start_col = col
			step = 1

			if (direction.startswith('R')):
				col = col + amount
			elif (direction.startswith('L')):
				col = col - amount
				step = -1
			elif (direction.startswith('U')):
				row = row - amount
				step = -1
			elif (direction.startswith('D')):
				row = row + amount
			else:
				print("ERROR unknown direction")
				exit(1)
			
			#print(f'{direction}: ({start_row},{start_col}) ==> ({row},{col}) amount: {amount} step: {step}') 
			
			if (direction.startswith('L') or direction.startswith('R')):
				# Walk Line
				for i in range(start_col+step, col+step, step):
					if (f'{row},{i}' in seen and seen[f'{row},{i}'] != wire): 
						intersections.append([row, i])
				
					steps = steps + 1
					seen[f'{row},{i}'] = wire
					wire_steps[wire][f'{row},{i}'] = steps

			else: # L | R
				# Walk Line
				for i in range(start_row+step, row+step, step):
					if (f'{i},{col}' in seen and seen[f'{i},{col}'] != wire):  
						intersections.append([i, col])
					
					# track
					steps = steps + 1
					seen[f'{i},{col}'] = wire
					wire_steps[wire][f'{i},{col}'] = steps
	
# Calulate shortest distance
for coords in intersections:	
	wire1_steps = wire_steps[0][f'{coords[0]},{coords[1]}'] 
	wire2_steps = wire_steps[1][f'{coords[0]},{coords[1]}'] 

	distance = wire1_steps + wire2_steps
	if (distance < shortest):
		shortest = distance


print(shortest)

print("\ndone.");

