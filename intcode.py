#!/usr/bin/env python3

import sys
from enum import IntEnum

class IntCode:
	
	def __init__(self, memory, input_vals=None, output_val=None):
		self.i_ptr = 0
		self.memory = memory
		self.output = output_val
		self.state = self.STATES.PAUSED
	
		# Support single input or list of inputs		
		if isinstance(input_vals, list): self.inputs = input_vals
		else: self.inputs = [input_vals]
		
		self.program_mappings = {
			self.OPCODES.ADD: self.add,
			self.OPCODES.MULTIPLY: self.multiply,
			self.OPCODES.COPY: self.copy,
			self.OPCODES.PRINT: self.print,
			self.OPCODES.JMP_IF_TRUE: self.jmp_if_true,
			self.OPCODES.JMP_IF_FALSE: self.jmp_if_false,
			self.OPCODES.LESS_THAN: self.less_than,
			self.OPCODES.EQUALS: self.equals,
			self.OPCODES.ENDPROGRAM: self.end_program,
		}

	class OPCODES(IntEnum):
		ADD = 1,
		MULTIPLY = 2,
		COPY = 3,
		PRINT = 4,
		JMP_IF_TRUE = 5,
		JMP_IF_FALSE = 6,
		LESS_THAN = 7,
		EQUALS = 8,
		ENDPROGRAM = 99

	class UNITS(IntEnum):
		AC = 1,
		THERML_RADI_CTLER = 5

	class MODES(IntEnum):
		POSITION = 0,
		IMMEDIATE = 1

	class STATES(IntEnum):
		PAUSED = 0,
		RUNNING = 1,
		ENDED = 2,

	def get_instruction(self, i_ptr):
		instruction = str(self.memory[i_ptr]).rjust(5, '0')
		op_code = int(instruction[-2:])
		modeA = int(instruction[2:3])
		modeB = int(instruction[1:2])
		modeC = int(instruction[0:1])
		#print(self.memory)
		#print(f'instruction: {instruction} i_ptr: {self.i_ptr} opcode: {op_code} modeA: {modeA} modeB: {modeB} modeC: {modeC}')
		return [op_code, modeA, modeB, modeC]

	def get_value(self, i_ptr, mode):		
		if (int(mode) == self.MODES.IMMEDIATE): return self.memory[i_ptr] # immediate
		else: return self.memory[int(self.memory[i_ptr])] # position
	
	def process(self):

		# run
		self.state = self.STATES.RUNNING

		# process
		while(self.state == self.STATES.RUNNING and self.i_ptr < len(self.memory)):
			instruction = self.get_instruction(self.i_ptr)
			operation = self.program_mappings[instruction[0]]
			operation(instruction)

			# Handle printing
			if (instruction[0] == self.OPCODES.PRINT or instruction[0] == self.OPCODES.ENDPROGRAM): 
				return self.output

		return False
		

	def add(self, instruction):
		valA = int(self.get_value(self.i_ptr + 1, instruction[1]))
		valB = int(self.get_value(self.i_ptr + 2, instruction[2]))
		posC = int(self.get_value(self.i_ptr + 3, 1))
		#print(f'i_ptr: {self.i_ptr} valA: {valA} valB: {valB} posC: {posC}')
		self.memory[posC] = valA + valB
		self.i_ptr+=4

	def multiply(self, instruction):
		valA = int(self.get_value(self.i_ptr + 1, instruction[1]))
		valB = int(self.get_value(self.i_ptr + 2, instruction[2]))
		posC = int(self.get_value(self.i_ptr + 3, 1))

		self.memory[posC] = valA * valB
		self.i_ptr+=4

	def copy(self, instruction):
		posA = int(self.get_value(self.i_ptr + 1, 1))
		intput  = str(self.inputs.pop(0))
		self.memory[posA] = intput
		self.i_ptr+=2

	def print(self, instruction):
		valA = self.get_value(self.i_ptr + 1, instruction[1])
	
		self.output = valA
		self.i_ptr+=2
		self.state = self.STATES.PAUSED

	def jmp_if_true(self, instruction):
		valA = int(self.get_value(self.i_ptr + 1, instruction[1]))
		valB = int(self.get_value(self.i_ptr + 2, instruction[2]))

		if (valA != 0): self.i_ptr = valB
		else: self.i_ptr+=3		

	def jmp_if_false(self, instruction):
		valA = int(self.get_value(self.i_ptr + 1, instruction[1]))
		valB = int(self.get_value(self.i_ptr + 2, instruction[2]))
	
		if (valA == 0): self.i_ptr = valB
		else: self.i_ptr+=3

	def less_than(self, instruction):
		valA = int(self.get_value(self.i_ptr + 1, instruction[1]))
		valB = int(self.get_value(self.i_ptr + 2, instruction[2]))
		posC = int(self.get_value(self.i_ptr + 3, 1))
		
		if (valA < valB): self.memory[posC] = 1
		else: self.memory[posC] = 0

		self.i_ptr+=4

	def equals(self, instruction):
		valA = int(self.get_value(self.i_ptr + 1, instruction[1]))
		valB = int(self.get_value(self.i_ptr + 2, instruction[2]))
		posC = int(self.get_value(self.i_ptr + 3, 1))

		if (valA == valB): self.memory[posC] = 1
		else: self.memory[posC] = 0

		self.i_ptr+=4

	def end_program(self, instruction):
		self.i_ptr+=1
		self.state = self.STATES.ENDED

