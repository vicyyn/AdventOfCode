#!/usr/bin/python3
import re

with open("../input.txt") as f:
    lines = f.read().strip().split('\n')

# Part 1
res = ''

stacks = [
        ['H','B','V','W','N','M','L','P'],
        ['M','Q','H'],
        ['N','D','B','G','F','Q','M','L'],
        ['Z','T','F','Q','M','W','G'],
        ['M','T','H','P'],
        ['C','B','M','J','D','H','G','T'],
        ['M','N','B','F','V','R'],
        ['P','L','H','M','R','G','S'],
        ['P','D','B','C','N'],
    ]

for line in lines:
    x = re.search(r"move (\d+) from (\d+) to (\d+)", line)
    if x:
        count , start , end = [int(i) for i in  x.groups()]
        while stacks[start - 1] and count > 0:
            stacks[end - 1].append(stacks[start - 1].pop())
            count -= 1

for stack in stacks:
    res = res + stack[-1] if stack else ' '

print(res)

# Part 2
res = ''

stacks = [
        ['H','B','V','W','N','M','L','P'],
        ['M','Q','H'],
        ['N','D','B','G','F','Q','M','L'],
        ['Z','T','F','Q','M','W','G'],
        ['M','T','H','P'],
        ['C','B','M','J','D','H','G','T'],
        ['M','N','B','F','V','R'],
        ['P','L','H','M','R','G','S'],
        ['P','D','B','C','N'],
    ]

for line in lines:
    x = re.search(r"move (\d+) from (\d+) to (\d+)", line)
    if x:
        count , start , end = [int(i) for i in  x.groups()]
        tempStack = []
        while stacks[start - 1] and count > 0:
            tempStack.append(stacks[start - 1].pop())
            count -= 1

        while tempStack:
            stacks[end - 1].append(tempStack.pop())

for stack in stacks:
    res = res + stack[-1] if stack else ' '

print(res)
