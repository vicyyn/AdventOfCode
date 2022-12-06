#!/usr/bin/python3

with open("../input.txt") as f:
    lines = f.read().strip().split('\n')

# Part 1
l = 0
curr = set()

for line in lines:
    for r in range(len(line)):
        while line[r] in curr:
            curr.remove(line[l])
            l += 1
        curr.add(line[r])
        if len(curr) == 4:
            print(r + 1)
            break

# Part 2
l = 0
curr = set()

for line in lines:
    for r in range(len(line)):
        while line[r] in curr:
            curr.remove(line[l])
            l += 1
        curr.add(line[r])
        if len(curr) == 14:
            print(r + 1)
            break
