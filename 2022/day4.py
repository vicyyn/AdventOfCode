#!/usr/bin/python3

with open("../input.txt") as f:
    lines = f.read().strip().split('\n')

# Part 1
res = 0

for line in lines:
    elf1 , elf2 = line.split(',')
    elf1start , elf1end = elf1.split('-')
    elf2start , elf2end = elf2.split('-')

    if (int(elf1start,10) >= int(elf2start,10) and int(elf1end,10) <= int(elf2end,10)) or (int(elf2start,10) >= int(elf1start,10) and int(elf2end,10) <= int(elf1end,10)):
        res += 1

print(res)

# Part 2
res = 0

for line in lines:
    elf1 , elf2 = line.split(',')
    elf1start , elf1end = elf1.split('-')
    elf2start , elf2end = elf2.split('-')

    if (int(elf1start,10) >= int(elf2start,10) and int(elf1start,10) <= int(elf2end,10)) or (int(elf2start,10) >= int(elf1start,10) and int(elf2start,10) <= int(elf1end,10)):
        res += 1

print(res)
