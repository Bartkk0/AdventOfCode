file = open('input.txt', 'r')
line = file.readline()

pos = 0
chars = []
for c in line:
    print(pos,chars)
    if c not in chars:
        chars.append(c)
    else:
        while c in chars:
            del chars[0]
        chars.append(c)

    if len(chars) == 14:
        break

    pos += 1

print("FLAG 2:", pos+1)
