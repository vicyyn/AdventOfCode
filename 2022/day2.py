#!/usr/bin/python3

with open("../input.txt") as f:
    lines = f.read().strip().split('\n')

# Part 1
res = 0

for line in lines:
    opp , player = line.split(' ')
    res += 1 + ord(player) - ord('X')
    if (player == "X" and opp == "A") or (player == "Y" and opp == "B") or (player == "Z" and opp == "C"):
        res += 3
    if (player == "X" and opp == "C") or (player == "Y" and opp == "A") or (player == "Z" and opp == "B"):
        res += 6

print(res)

# Part 1
res = 0

for line in lines:
    opp , player = line.split(' ')
    res += (ord(player) - ord('X')) * 3
    if player == 'Y':
        res += 1 + ord(opp) - ord('A')
    elif player == 'Z':
        if opp == "C":
            res += 1
        else:
            res += 2 + ord(opp) - ord('A')
    else:
        if opp == "A":
            res += 3
        else:
            res += ord(opp) - ord('A')

print(res)
