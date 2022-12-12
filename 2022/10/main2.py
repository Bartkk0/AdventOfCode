import math

file = open('input.txt','r')

global flag1,current_line
flag2 = [''] * 10
current_line = ""
cycles = 0
X = 1

def state():
    global flag2, current_line
    # print(cycles, X)
    x = cycles%40
    y = math.floor((cycles-1)/40)
    print(x,y)

    if X <= x <= X+2:
        flag2[y] += "█"
    else:
        flag2[y] += "."

for line in file:
    line = line.strip()

    if line == "noop":
        cycles += 1
        state()
    else:
        split = line.split(' ')
        num = int(split[1])
        cycles += 1
        state()
        cycles += 1
        state()
        X += num

for l in flag2:
    print(l)
