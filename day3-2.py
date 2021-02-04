with open("input.txt") as f:
    lines = f.read().strip().split('\n')
dat = [x for x in lines]
total2 = 0

def getNumberOfTrees(xslope,yslope):
    x = 0
    y = 0
    total = 0
    while y < len(dat): 
        if(dat[y][x] == '#'):
            total = total +1
        x = (x+xslope) % len(dat[0])
        y = y+yslope
    return total

total2 = getNumberOfTrees(1,1) * getNumberOfTrees(7,1) * getNumberOfTrees(5,1) * getNumberOfTrees(3,1) * getNumberOfTrees(1,2)
print(total2)

