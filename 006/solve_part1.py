#!/usr/bin/env python3

import sys


if len(sys.argv) != 2:
	print("usage: solve.py input.txt")
	exit(1)



def count_paths(node, count, depth):
	#print(f'{node}: count: {count} depth: {depth}')

	children = graph[node]

	# leaf
	if not children: return count

	# process childen
	for child_node in children:
		depth = depth+1
		count = depth + count_paths(child_node, count, depth)
		depth = depth-1
	
	return count

# Build Graph
graph = {}
edges = []
with open(sys.argv[1]) as f:
	data = f.read()
	lines = data.splitlines()

	for line in lines:		
		nodes = line.split(")")

		if not (nodes[0] in graph): graph[nodes[0]] = []
		if not (nodes[1] in graph): graph[nodes[1]] = []

		# Add Nodes to Graph
		graph[nodes[0]].append(nodes[1])

		# Create Edges
		edges.append([nodes[0], nodes[1]])

# Traverse the nodes
paths_count = count_paths('COM', 0, 0)


print(f'Answer: {paths_count}')
#print(graph)
print("\ndone.");

