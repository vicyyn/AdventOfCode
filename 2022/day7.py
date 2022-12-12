#!/usr/bin/python3

with open("../input.txt") as f:
    lines = f.read().strip().split('\n')

# Part 1
res = 0
folders = {}
pwd = '/'
sizes = {}


i = 0
while i < len(lines):
    line = lines[i]
    args = line.split(' ')
    if args[1] == 'cd':
        if args[2] == '/':
            pwd = '/'
        elif args[2] == '..':
            pwd = pwd[0:pwd[0:pwd.rfind('/')].rfind('/') + 1]
        else:
            pwd = pwd + args[2] + '/'
    else:
        folders[pwd] = []
        while i + 1 < len(lines) and lines[i + 1].split(' ')[0] != '$':
            line = lines[i + 1].split(' ')
            if line[0] == 'dir':
                folders[pwd].append(pwd + line[1] + '/')
            else:
                folders[pwd].append(line[0])
            i += 1

    i += 1

def getFolderSize(element):
    if element not in folders:
        return int(element,10)

    res = 0
    for child in folders[element]:
        res += getFolderSize(child)
    return res

for folder in folders:
    size = getFolderSize(folder)
    if size <= 100000:
        res += size

print(res)

# Part2
total = getFolderSize('/')
needed = 30000000 - (70000000 - total)

minFolder = total
for folder in folders:
    size = getFolderSize(folder)
    if size >= needed:
        minFolder = min(minFolder,size)

print(minFolder)




