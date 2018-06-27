'''
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
'''
full = []
pad = input()
full.append(pad)

while True:
    pad = input()
    d = pad.split(' ')
    if not pad:
        break
    full.append(d)

for i in full:
    if len(i) != 3:
        full.remove(i)

global_env = []

for i in full:
    if i[0] != "get":
        print(i)