t = int(input("Enter: "))

l = []
for i in range(t):
    n = int(input("Enter: "))
    if n > 1000:
        j = n//1000
        n = n - j*1000
        l.append(j*1000)
    if n > 100:
        j = n//100
        n = n - j*100
        l.append(j*100)
    if n > 10:
        j = n//10
        n = n - j*10
        l.append(j*10)
    if n > 0:
        l.append(n)
        n = 0
    k = ""
    print(len(l))
    for i in l:
        k += f"{i} "
    print(k)
    k = ""
    l = []
