with open("input.txt") as f:
    lines = f.read().strip().split('\n')
dat = [x for x in lines]
total = 0
x = 0
y = 0

while y < len(dat): 
    if(dat[y][x] == '#'):
        total = total +1
    x = (x+3) % len(dat[0])
    y = y+1
print(total)
