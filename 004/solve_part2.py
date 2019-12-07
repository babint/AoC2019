#!/usr/bin/env python3

import sys
from itertools import groupby
from operator import itemgetter

if len(sys.argv) != 3:
    print("usage: solve.py 123 456")
    exit(1)

start = int(sys.argv[1])
end = int(sys.argv[2])

passwords = []
for password in range(start, end):
	password = str(password)
	is_valid = True

	# Length Check
	if (len(password) != 6): continue

	# Check is Incrementing
	last = -1
	for curr in password:
		if (int(curr) < int(last)): is_valid = False
		last = curr
	if (not is_valid): continue
	
	# Check for single adj repeat
	last = -1
	dup_counts = [0,0,0,0,0,0,0,0,0,0]
	for curr in password:
		curr = int(curr)
		if (curr != last): 
			last = curr
			continue
		dup_counts[curr] = dup_counts[curr] + 1
		last = curr

	# verify  dups
	dup_check = False
	## TODO

	if (not dup_check): is_valid = False
	if (not is_valid): continue

	# Checks out
	passwords.append(password)		

print(passwords)
print(f'len: {len(passwords)}')
print("\ndone.");

