fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
def process(passport):
    if(all(substring in passport for substring in fields)):
        return True
    else:
        return False
    
with open("input.txt") as f:
    dat = f.readlines()
    dat = [line.strip() for line in dat]

total = 0
currentPassport = ''
for i in dat:
    if i != '':
       currentPassport += ' ' + i
    else:
        if(process(currentPassport)):
            total += 1
        currentPassport = ''

if(process(currentPassport)):
    total += 1

print(total)
