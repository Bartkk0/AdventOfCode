file = open('input.txt', 'r')
lines = file.readlines()

def parse_pair(input):
    out = [[],[]]
    split = input.split(',')
    out[0] = split[0].split('-')
    out[1] = split[1].split('-')

    out[0][0] = int(out[0][0])
    out[0][1] = int(out[0][1])
    out[1][0] = int(out[1][0])
    out[1][1] = int(out[1][1])
    return out

def pair_in_pair(pair):
    a = pair[0]
    b = pair[1]
    return (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1])

def pair_overlaps_pair(pair):
    a = pair[0]
    b = pair[1]
    return (a[0] <= b[0] <= a[1]) or (a[0] <= b[1] < a[1]) or (b[0] <= a[0] <= b[1]) or (b[0] <= a[1] < b[1])

flag1 = 0
for line in lines:
    line = line.strip()
    pair = parse_pair(line)
    if pair_in_pair(pair):
        flag1 += 1
print("FLAG 1:", flag1)

flag2 = 0
for line in lines:
    line = line.strip()
    pair = parse_pair(line)
    if pair_overlaps_pair(pair):
        flag2 += 1
print("FLAG 2:", flag2)
