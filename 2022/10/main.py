file = open('input.txt','r')

check = [20,60,100,140,180,220]

global flag1
flag1 = 0
cycles = 0
X = 1

def state():
    global flag1
    print(cycles, X)

    if cycles in check:
        flag1 += X * cycles

for line in file:
    line = line.strip()
    print(line)

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

print("FLAG1:",flag1)
