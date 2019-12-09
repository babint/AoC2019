#!/usr/bin/env python3

import sys


if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)

graph = {}
start_node = "COM"

def count_paths(node, count, depth, visited):
	#print(f'{node}: count: {count} depth: {depth} visited: {visited}')

	# Mark node as seen this path
	visited.append(node)
	
	# process childen
	for child_node in graph[node]:
		if (child_node in visited): continue
		count = (depth+1) + count_paths(child_node, count, (depth+1), visited)
	
	return count

# Build Graph
with open(sys.argv[1]) as f:
	data = f.read()
	lines = data.splitlines()

	for line in lines:		
		nodes = line.split(")")

		# Init
		if not (nodes[0] in graph): graph[nodes[0]] = []
		if not (nodes[1] in graph): graph[nodes[1]] = []

		# Add Nodes to Graph (bi-directional)
		graph[nodes[0]].append(nodes[1])
		graph[nodes[1]].append(nodes[0])


# Traverse the nodes
paths_count = count_paths(start_node, 0, 0, [])

#print(graph)
print(f'Answer: {paths_count}')
#print(graph)
print("\ndone.");

