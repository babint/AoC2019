#!/usr/bin/env python3

import sys
from enum import IntEnum
import copy 

class Opcodes(IntEnum):
	ADD = 1,
	MULTIPLY = 2,
	COPY = 3,
	PRINT = 4,
	JMP_IF_TRUE = 5,
	JMP_IF_FALSE = 6,
	LESS_THAN = 7,
	EQALS = 8,
	ENDPROGRAM = 99

class units(IntEnum):
	AC = 1,
	THERML_RADI_CTLER = 5

class modes(IntEnum):
	POSITION = 0,
	IMMEDIATE = 1

def processMemory(memory, input_val):
	output_val = False
	
	i_ptr = 0
	while (i_ptr < len(memory)):
		instruction = str(memory[i_ptr]).rjust(5, '0')
		op_code = int(instruction[-2:])
	
		#print(f'instruction: {instruction} op_code: {op_code} i_ptr: {i_ptr} input_val: {input_val}')
		
		# Halt on request
		if (op_code == Opcodes.ENDPROGRAM): break

		modeA = int(instruction[2:3])
		modeB = int(instruction[1:2])
		modeC = int(instruction[0:1])
		posA = int(memory[i_ptr+1])
		
		posB = False
		posC = False
	
		if ((i_ptr+2) < len(memory)):
			posB = int(memory[i_ptr+2])		
		if ((i_ptr+3) < len(memory)):
			posC = int(memory[i_ptr+3])	

		#print(f'posA: {posA} posB: {posB} posC: {posC}')
		#print(f'modeA: {modeA} modeB: {modeB} modeC: {modeC}')
		#print(f'memA: {memory[posA]} memB: {int(memory[posB])}')

		if (modeA == modes.POSITION):
			valA = memory[posA]
		else: 
			valA = posA

		if (op_code != Opcodes.COPY and op_code != Opcodes.PRINT):			
			if (modeB == modes.POSITION):
				valB = memory[posB]
			else: 
				valB = posB
		if (
				op_code != Opcodes.COPY
				and op_code != Opcodes.PRINT 
				and op_code != Opcodes.JMP_IF_FALSE 
				and op_code != Opcodes.JMP_IF_TRUE and op_code != Opcodes.LESS_THAN
		):	
			if (modeC == modes.POSITION):
				valC = memory[posC]
			else: 
				valC = posC

		if (op_code == Opcodes.ADD or op_code == Opcodes.MULTIPLY):	
			
			# Peform Operation
			if (op_code == Opcodes.ADD): 
				#print(f'writing: ({memory[posA]} + {memory[posB]}) to pos: {posC}')
				memory[posC] = int(valA) + int(valB)
			elif(op_code == Opcodes.MULTIPLY):
				memory[posC] = int(valA) *  int(valB)
			
			# Move ptr to next instruction
			i_ptr = i_ptr + 4
		elif (op_code == Opcodes.COPY):
			memory[posA] = str(input_val)
			i_ptr = i_ptr + 2
		
		elif (op_code == Opcodes.PRINT):
			output_val = valA			
			i_ptr = i_ptr + 2			
		elif (op_code == Opcodes.JMP_IF_TRUE):
			if (int(valA) != 0): 
				i_ptr = int(valB)
			else:	
				i_ptr = i_ptr + 3
		elif (op_code == Opcodes.JMP_IF_FALSE):
			if (int(valA) == 0): 
				i_ptr = int(valB)
			else:	
				i_ptr = i_ptr + 3
		elif (op_code == Opcodes.LESS_THAN):
			if (int(valA) < int(valB)): 
				memory[posC] = 1
			else:
				memory[posC] = 0
			i_ptr = i_ptr + 4
		elif (op_code == Opcodes.EQALS):
			if (int(valA) == int(valB)): 
				memory[posC] = 1
			else:
				memory[posC] = 0
			i_ptr = i_ptr + 4
		else:
			print(f'Error - Invalid opcode: {op_code} i_ptr: {i_ptr}')
			print(memory)
			exit(1)

	return output_val

if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

memory = []
# Load data into memory
with open(sys.argv[1]) as f:
	data = f.read()
	memory = data.split(",")

	output = processMemory(memory, 5)
	print(f'output: {output}')


print("\ndone.");

