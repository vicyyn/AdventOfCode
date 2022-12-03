#!/usr/bin/python3
import string

with open("../input.txt") as f:
    lines = f.read().strip().split('\n')

# Part 1
res = 0
graph = {}

for line in lines:
    for i in range(len(line) // 2):
        graph[line[i]] = True

    for i in range(len(line) // 2,len(line)):
        if graph.get(line[i],False):
            graph[line[i]] = False
            if line[i] in string.ascii_lowercase:
                res += ord(line[i]) - ord('a') + 1
            else:
                res += ord(line[i]) - ord('A') + 27

    graph.clear()

print(res)

# Part 2
res = 0
graph = {}
i = 0 

for line in lines:
    if i == 0:
        for c in line:
            graph[c] = True
    if i == 1:
        grapht = {}
        for c in line:
            if graph.get(c,False) == True:
                grapht[c] = True
        graph = grapht
    if i == 2:
        grapht = {}
        for c in line:
            if graph.get(c,False) == True:
                grapht[c] = True
        graph = grapht

        for c in graph:
            graph[c] = False
            if c in string.ascii_lowercase:
                res += ord(c) - ord('a') + 1
            else:
                res += ord(c) - ord('A') + 27
        graph.clear()
        i = -1

    i+= 1

print(res)
