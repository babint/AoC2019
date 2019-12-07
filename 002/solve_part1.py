#!/usr/bin/env python3

import sys
from enum import IntEnum

class Opcodes(IntEnum):
    ADD = 1,
    MULTIPLY = 2,
    ENDPROGRAM = 99


if len(sys.argv) != 2:
    print("usage: solve.py input.txt")
    exit(1)

lines = []
with open(sys.argv[1]) as f:
	data = f.read()
	lines = data.split(",")

	for i in range(0, len(lines), 4):
		opcode = int(lines[i])
		
		# Halt on request
		if (opcode == Opcodes.ENDPROGRAM): break

		posA = int(lines[i+1])
		posB = int(lines[i+2])
		posC = int(lines[i+3])
		if (opcode == Opcodes.ADD): 
			lines[posC] = int(lines[posA]) + int(lines[posB])
		elif(opcode == Opcodes.MULTIPLY):
			lines[posC] = int(lines[posA]) *  int(lines[posB])
		else: 
			print("ERROR")



print(lines)
print("\ndone.");

