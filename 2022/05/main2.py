import re

containers = []
for i in range(12):
    containers.append([])

file = open('input.txt', 'r')
lines = file.readlines()

containers = []
for i in range(12):
    containers.append([])

line_i = 0
for line in lines:
    line_i += 1
    if line[1] == '1':
        break

    col = 0
    for c in map(''.join, zip(*[iter(line)]*4)):
        if c[0] == '[':
            containers[col].insert(0,c[1])
        col += 1
print(containers)

r = re.compile('move (\\d*) from (\\d*) to (\\d*)')
for line in lines[line_i+1:]:
    line = line.strip()
    print(containers)
    print(line,'\n')
    line = line.strip()
    m = r.findall(line)[0]
    tmp = []
    for i in range(int(m[0])):
        tmp.append(containers[int(m[1])-1].pop())
    print(tmp)
    for t in tmp[::-1]:
        containers[int(m[2])-1].append(t)

flag1 = ''
for c in containers:
    if len(c) != 0:
        flag1 += c[len(c)-1]
print("FLAG 1:",flag1)

