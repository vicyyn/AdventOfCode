#!/usr/bin/python3

import heapq

with open("../input.txt") as f:
    lines = f.read().strip().split('\n')

# Part 1
res = 0
currentSum = 0

for line in lines:
    if not line:
        currentSum = 0
    else:
        currentSum += int(line,10)
    res = max(res,currentSum)

print(res)

# Part 2
heap = []
currentSum = 0

for line in lines:
    if not line:
        heapq.heappush(heap,-currentSum)
        currentSum = 0
    else:
        currentSum += int(line,10)

res = -1 * (heapq.heappop(heap) + heapq.heappop(heap) + heapq.heappop(heap))
print(res)
