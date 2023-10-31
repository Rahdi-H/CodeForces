n, m = list(map(int, input("Enter: ").split(" ")))

t = list(map(int, input("Enter: ").split(" ")))

t.sort()
e = 0
for i in t:
    if i < 0 and m != 0:
        e += i
        m -= 1

print(abs(e))
