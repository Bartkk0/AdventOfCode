file = open('input.txt','r')
lines = file.readlines()

def str_to_dict(string):
    dict = {}
    for c in string:
        if c not in dict:
            dict[c] = 0
        dict[c] += 1
    return dict

def priority(a):
    if a.islower():
        return ord(a) - 96
    elif a.isupper():
        return ord(a) - 65 + 27
    print("UNSUPPORTED PRIORITY: ", a)

priority_sum = 0
for line in lines:
    line = line.strip()
    half_length = int(len(line) / 2)

    a = line[:half_length]
    b = line[half_length:]

    aa = str_to_dict(a)
    bb = str_to_dict(b)

    for k in aa:
        if k in bb:
            # print(k, priority(k))
            priority_sum += priority(k)
print("FLAG 1: ", priority_sum)

flag2_sum = 0
for i in range(0,len(lines)-1,3):
    a = lines[i].strip()
    b = lines[i+1].strip()
    c = lines[i+2].strip()

    aa = str_to_dict(a)
    bb = str_to_dict(b)
    cc = str_to_dict(c)

    for k in aa:
        if k in bb and k in cc:
            print(k)
            flag2_sum += priority(k)
print("FLAG 2: ", flag2_sum)
