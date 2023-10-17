import math
t = int(input("sdf "))

for _ in range(t):
    a, b = list(map(int, input("df ").split(" ")))
    c = 0
    i = 2
    while (a % b != 0):
        if a < b:
            c = b - a
            a = c + b
            break
        if b*i > a:
            c = b*i - a
            a = b*i
            i = 2
        elif a/2 > b:
            j = a / b
            k = math.ceil(j)
            c += (k*b - a)
            a += c
        else:
            i += 1
    print(c)
