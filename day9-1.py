with open("input.txt") as f:
    dat = f.readlines()
    dat = [line.strip() for line in dat]
    s=0
    j=-1
    for l in dat:
        j=j+1
        i=-1
        for v in l:
            i=i+1
            if(i==0 and j==0):
                if(int(v)< int(l[1]) and int(v)< int(dat[1][0])):
                    s = s +int(v) +1
                continue

            if(i==len(l)-1 and j==0):
                if(int(v)< int(l[len(l)-2]) and int(v)< int(dat[1][len(l)-1])):
                    s = s +int(v) +1
                continue

            if(j==len(dat)-1 and i==0):
                if(int(v)< int(l[1]) and int(v)< int(dat[len(dat)-2][0])):
                    s = s +int(v)+1
                continue

            if(j==len(dat)-1 and i==len(l)-1):
                if(int(v)< int(l[len(l)-2]) and int(v)< int(dat[len(dat)-2][len(l)-1])):
                    s = s +int(v)+1
                continue

            if(j==0):
                if(int(v)< int(l[i-1]) and int(v)<int(l[i+1]) and int(v)< int(dat[j+1][i])):
                    s = s +int(v)+1
                continue

            if(j==len(dat)-1):
                if(int(v)< int(l[i-1]) and int(v)<int(l[i+1]) and int(v)< int(dat[j-1][i])):
                    s = s +int(v)+1
                continue

            if(i==0):
                if(int(v)< int(l[i+1]) and int(v)<int(dat[j-1][i]) and int(v)< int(dat[j+1][i])):
                    s = s +int(v)+1
                continue

            if(i==len(l)-1):
                if(int(v)< int(l[i-1]) and int(v)<int(dat[j-1][i]) and int(v)< int(dat[j+1][i]) ):
                    s = s +int(v)+1
                continue

            if(int(v)< int(l[i-1]) and int(v) < int(l[i+1]) and int(v)<int(dat[j-1][i]) and int(v)< int(dat[j+1][i])):
                s = s +int(v)+1

    print(s)

