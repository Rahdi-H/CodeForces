n, k = list(map(int, input("Enter: ").split(" ")))
t = 240 - k
p = 0
pt = 0
for i in range(1, n+1):
    if (pt + (i * 5)) <= t:
        pt += i*5
        p += 1
    else:
        break

print(p)
