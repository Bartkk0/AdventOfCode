file = open('input.txt', 'r')

width = 0
height = 0

trees = []
for line in file:
    line = line.strip()
    row = []
    for c in line:
        row.append(int(c))
    trees.append(row)
    width = len(row)
height = len(trees)
print(trees)

def check_visibility(x,y):
    h = trees[y][x]

    up = 0
    for i in range(y-1,-1,-1):
        up += 1
        if trees[i][x] >= h:
            break
    down = 0
    for i in range(y+1,height):
        down += 1
        if trees[i][x] >= h:
            break

    left = 0
    for i in range(x-1,-1,-1):
        left += 1
        if trees[y][i] >= h:
            break

    right = 0
    for i in range(x+1,width):
        right += 1
        if trees[y][i] >= h:
            break

    # print(up,left,right,down)
    
    return up * left * down * right

    
print(check_visibility(2,1))
max = 0
for y in range(height):
    for x in range(width):
        vis = check_visibility(x,y) 
        if vis > max:
            max = vis
        print(vis,end=" ")
    print()
print("FLAG2:",max)
