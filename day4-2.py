import re
import string

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
ecl_fields = 'amb blu brn gry grn hzl oth'.split(' ')

def process(passport):
    if(all(substring in passport for substring in fields)):
        passportList = re.split(' ',passport)
        passportList = [i for i in passportList if(i != '')]
        for element in passportList:
            if(fields[0] in element):
                element = element.split(':')[1]
                if(int(element) < 1920 or int(element) > 2002):
                    return(False)
            if(fields[1] in element):
                element = element.split(':')[1]
                if(int(element) < 2010 or int(element) > 2020):
                    return(False)
            if(fields[2] in element):
                element = element.split(':')[1]
                if(int(element) < 2020 or int(element) > 2030):
                    return(False)
            if(fields[3] in element):
                element = element.split(':')[1]
                if('cm' in element):
                    element = element.replace('cm','')
                    if(int(element) < 150 or int(element) > 193):
                        return(False)
                if('in' in element):
                    element = element.replace('in','')
                    if(int(element) < 59 or int(element) > 76):
                        return(False)
            if(fields[4] in element):
                element = element.split(':')[1]
                if(element[0] != '#'):
                    return(False)
                element = element.replace('#','')
                if(any(c not in string.hexdigits for c in element) and len(element) != 6):
                    return(False)
            if(fields[5] in element):
                if(all(substring not in element for substring in ecl_fields)):
                    return(False)
            if(fields[6] in element):
                element = element.split(':')[1]
                if(not re.match('^[0-9]{9}$',element)):
                    return False
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

