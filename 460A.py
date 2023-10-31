n, m = list(map(int, input('Enter: ').split(" ")))
c = 0
k = m
while n != 0:
    m -= 1
    n -= 1
    c += 1
    if m == 0:
        n += 1
        m = k
print(c)
