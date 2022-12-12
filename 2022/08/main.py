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
    if x == 0 or y == 0:
        return True
    if x == width - 1 or y == height - 1:
        return True

    h = trees[y][x]

    if all(trees[i][x] < h for i in range(y-1,-1,-1)):
        return True
    if all(trees[i][x] < h for i in range(y+1,height)):
        return True
    if all(trees[y][i] < h for i in range(x-1,-1,-1)):
        return True
    if all(trees[y][i] < h for i in range(x+1,width)):
        return True
    return False

flag1 = 0
for y in range(height):
    for x in range(width):
        vis = check_visibility(x,y) 
        if vis:
            flag1 += 1
        print(trees[y][x] if vis else ' ',end="")
    print()
print("FLAG1:",flag1)
