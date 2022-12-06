file = open('input.txt', 'r')
line = file.readline()

pos = 0
streak = 0
chars = []
for c in line:
    if c not in chars:
        streak += 1
        chars.append(c)
        if streak == 4:
            break
    else:
        streak = 0
        chars = []
    pos += 1

print("FLAG 1:", pos)


