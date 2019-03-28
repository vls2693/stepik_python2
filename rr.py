"""
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
"""
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
        if i[1] == "global":
            global_env.append(i[2])
        if i[2] == "global":
            global_env.append(i[1])


print(global_env)

for l in range(0, len(full)):
    for i in full:
        if i[0] != "get":
            if i[1] == 'global':
                full.remove(i)
            elif i[2] == 'global':
                full.remove(i)
            else:
                continue
        else:
            continue

print(full)
exist = []
for i in range(0, len(global_env)):
    exist.append('x')
print(exist)
for i in range(0, 1):
    if full[i][1] in global_env:
        print(global_env.index(full[i][1]))
        print(global_env[global_env.index(full[i][1])][0])
        print(global_env[global_env.index(full[i][1])][1])
        print(global_env[global_env.index(full[i][1])][2])

for i in range(0, len(exist)):
    exist[i].append('r')
print(exist)
