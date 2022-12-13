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

# Part 2
ROWS , COLS = len(arr) , len(arr[0])
res = 1


for r in range(1,ROWS - 1):
    for c in range(1,COLS - 1):
        node = arr[r][c]
        up , down , right , left = 1 , 1 , 1 , 1 
        for i in range(c + 1,COLS):
            if arr[r][i] < node:
                right += 1
            else:
                break

        for i in range(c - 1,-1,-1):
            if arr[r][i] < node:
                left += 1
            else:
                break

        for i in range(r + 1,ROWS):
            if arr[i][c] < node:
                up += 1
            else:
                break

        for i in range(r - 1,-1,-1):
            if arr[i][c] < node:
                down += 1
            else:
                break

        res = max(res,up * down * right * left)

print(res)
