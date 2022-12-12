#!/usr/bin/python3

# https://github.com/juanplopes/advent-of-code-2022/blob/main/day10.py
def execute(program):
    X = 1
    for line in program:
        yield X
        if line[0] == 'addx':
            yield X
            X += int(line[1])

with open("../input.txt") as f:
    lines = f.read().strip().split('\n')

# Part 1
S = list(execute(line.split() for line in lines))
print(sum(S[i-1]*i for i in [20, 60, 100, 140, 180, 220]))

# Part 2
for i in range(6):
    print(''.join('.#'[abs(S[i*40+j] - j) <= 1] for j in range(40)))
