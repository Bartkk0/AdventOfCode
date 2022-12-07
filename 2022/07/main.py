# <warning>
# Shitty code ahead
# </warning>

import fs

mfs = fs.open_fs('mem://')

file = open('input.txt', 'r')
file.readline()

files = {}
state = 'CMD'
current_dir = '/'

def create_dir(name):
    print('Creating directory',name)
    mfs.makedir(current_dir+name)

def create_file(name, size):
    print('Creating file',name,'Size:',size)
    mfs.writetext(current_dir+'/'+name,str(size))

while line := file.readline().strip():
    if line.startswith('$'):
        state = 'CMD'

    if state == 'CMD':
        split = line.split(' ')
        cmd = split[1]
        if cmd == 'ls':
            state = 'LS'
            continue
        if cmd == 'cd':
            print('Change directory to', split[2])
            current_dir += split[2] + '/'
            continue
    
    if state == 'LS':
        split = line.split(' ')
        name = split[1]
        if split[0] == 'dir':
            create_dir(name)
        else:
            create_file(name,int(split[0]))

global flag1
flag1 = 0
def calculate_size_1(path,depth=0):
    global flag1
    size = 0
    for f in mfs.listdir(path):
        if mfs.isdir(path+'/'+f):
            print(f"{' '*depth*2} - {f} (dir)")
            s = calculate_size_1(path+'/'+f,depth+1)
            if s <= 100000:
                flag1 += s
            size += s
        else:
            s = int(mfs.readtext(path+'/'+f))
            print(f"{' '*depth*2} - {f} (file, size={s})")
            size += s
    return size

calculate_size_1('')
print(flag1)

print('------------')

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000

def calculate_size(path,depth=0):
    size = 0
    for f in mfs.listdir(path):
        if mfs.isdir(path+'/'+f):
            print(f"{' '*depth*2} - {f} (dir)")
            s = calculate_size(path+'/'+f,depth+1)
            size += s
        else:
            s = int(mfs.readtext(path+'/'+f))
            print(f"{' '*depth*2} - {f} (file, size={s})")
            size += s
    return size
free_space = TOTAL_SPACE - calculate_size('')
print("Free space:",free_space)

global flag2
flag2 = 9999999999
def calculate_size_2(path,depth=0):
    global flag2
    size = 0
    for f in mfs.listdir(path):
        if mfs.isdir(path+'/'+f):
            print(f"{' '*depth*2} - {f} (dir)")
            s = calculate_size_2(path+'/'+f,depth+1)
            print(s)
            if s >= REQUIRED_SPACE - free_space:
                if s < flag2:
                    flag2 = s
            size += s
        else:
            s = int(mfs.readtext(path+'/'+f))
            print(f"{' '*depth*2} - {f} (file, size={s})")
            size += s
    return size

calculate_size_2('')
print(flag2)
