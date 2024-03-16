a = [[0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0]]

inpt = input()


i = 1
ax = 1
for ch in inpt:
    if ch == 'L':
        ax -= 1
    if ch == 'R':
        ax += 1
    if ax == 0 or ax == 1: 
        a[ax][i] = 1
        i += 1
    else:
        print('DEATH')
        exit()

print("".join(str(x) for x in a[0]))
print("".join(str(x) for x in a[1]))