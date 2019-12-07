#!/usr/bin/env python3

import sys
from enum import IntEnum
import copy 

INSTRUCTION_SIZE = 4

class Opcodes(IntEnum):
    ADD = 1,
    MULTIPLY = 2,
    ENDPROGRAM = 99

def processMemory(memory):
	for i_ptr in range(0, len(memory), INSTRUCTION_SIZE):
		op_code = int(memory[i_ptr])

		# Halt on request
		if (op_code == Opcodes.ENDPROGRAM): break

		noun = int(memory[i_ptr+1])
		verb = int(memory[i_ptr+2])
		posC = int(memory[i_ptr+3])
		if (op_code == Opcodes.ADD): 
			memory[posC] = int(memory[noun]) + int(memory[verb])
		elif(op_code == Opcodes.MULTIPLY):
			memory[posC] = int(memory[noun]) *  int(memory[verb])
		else: 
			print("ERROR")
	
	return memory


if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

memory = []
# Load data into memory
with open(sys.argv[1]) as f:
	data = f.read()
	memory = data.split(",")

	for i in range(0,100):
		for j in range(0,100):
			new_memory = copy.copy(memory)
			memory[1] = i
			memory[2] = j
			new_memory = processMemory(new_memory)
			
			if (new_memory[0] == 19690720):
				print(f'Answer: i: {i} j: {j} {new_memory[0]}')
				print(new_memory)





print("\ndone.");

