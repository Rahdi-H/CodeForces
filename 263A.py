m = []
for _ in range(5):
    i = input().split(" ")
    m.append(i)
r = 0
c = 0
for o, i in enumerate(m):
    for j, k in enumerate(i):
        if k == '1':
            r = o + 1
            c = j + 1
            break
m = 0
while (r > 3):
    r -= 1
    m += 1
while (c > 3):
    c -= 1
    m += 1
while (r < 3):
    r += 1
    m += 1
while (c < 3):
    c += 1
    m += 1

print(m)
