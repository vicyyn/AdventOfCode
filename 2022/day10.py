#!/usr/bin/python3

with open("../input.txt") as f:
    lines = f.read().strip().split('\n')

# Part 1
cycles = 0
register = 1
signal_strengths = {}

for line in lines:
    args = line.split(' ')
    if args[0] == "noop":
        cycles += 1
        signal_strengths[cycles] = register * cycles
    else:
        cycles += 1
        signal_strengths[cycles] = register * cycles
		
        cycles += 1
        signal_strengths[cycles] = register * cycles
        register += int(args[1])

res = sum(signal_strengths.get(i, 0) for i in range(20, 221, 40))
print(res)

