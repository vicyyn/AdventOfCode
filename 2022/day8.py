#!/usr/bin/python3

with open("../input.txt") as f:
    lines = f.read().strip().split('\n')

# Part 1
arr = []
res = 0

for line in lines:
    arr.append(list(map(int,line)))

ROWS , COLS = len(arr) , len(arr[0])
res += 2 * ROWS + 2 * COLS - 4
added = set()

for r in range(1,ROWS - 1):
    for c in range(1,COLS - 1):
        if (r,c) not in added and (arr[r][c] > arr[0][c] or arr[r][c] > arr[r][0]):
            added.add((r,c))
            res += 1

        arr[0][c] = max(arr[r][c],arr[0][c])
        arr[r][0] = max(arr[r][c],arr[r][0])

for r in range(ROWS-2,0, - 1):
    for c in range(COLS-2,0,- 1):
        if (r,c) not in added and (arr[r][c] > arr[ROWS-1][c] or arr[r][c] > arr[r][COLS-1]):
            added.add((r,c))
            res += 1

        arr[ROWS-1][c] = max(arr[r][c],arr[ROWS-1][c])
        arr[r][COLS-1] = max(arr[r][c],arr[r][COLS-1])

print(res)
