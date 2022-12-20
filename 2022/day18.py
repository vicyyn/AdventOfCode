#!/usr/bin/python3

arr = []
with open("../input.txt") as f:
    lines = f.read().strip().split('\n')

# Part 1
x_vertices = set()
y_vertices = set()
z_vertices = set()

for line in lines:
    x , y , z = line.split(',')
    if (int(x),int(y),int(z)) in x_vertices:
        x_vertices.remove((int(x),int(y),int(z)))
    else:
        x_vertices.add((int(x),int(y),int(z)))
        
    if (int(x)+1,int(y),int(z)) in x_vertices:
        x_vertices.remove((int(x)+1,int(y),int(z)))
    else:
        x_vertices.add((int(x)+1,int(y),int(z)))

    if (int(x),int(y),int(z)) in y_vertices:
        y_vertices.remove((int(x),int(y),int(z)))
    else:
        y_vertices.add((int(x),int(y),int(z)))
        
    if (int(x),int(y)+1,int(z)) in y_vertices:
        y_vertices.remove((int(x),int(y)+1,int(z)))
    else:
        y_vertices.add((int(x),int(y)+1,int(z)))

    if (int(x),int(y),int(z)) in z_vertices:
        z_vertices.remove((int(x),int(y),int(z)))
    else:
        z_vertices.add((int(x),int(y),int(z)))
        
    if (int(x),int(y),int(z)+1) in z_vertices:
        z_vertices.remove((int(x),int(y),int(z)+1))
    else:
        z_vertices.add((int(x),int(y),int(z)+1))


print(len(x_vertices) + len(y_vertices) + len(z_vertices))

# Part 2
