n = int(input("Enter: "))
p = list(map(int, input("Enter: ").split(" ")))
q = list(map(int, input("Enter: ").split(" ")))
if p[0] + q[0] < n:
    print("Oh, my keyboard!")
else:
    a = 0
    del p[0]
    del q[0]
    p.sort()
    q.sort()
    p.extend(q)
    k = set(p)
    o = list(k)
    c = 1
    for i in o:
        if i == c:
            c += 1
        else:
            a = 1
            print("Oh, my keyboard!")
            break
    if c > n and a == 0:
        print("I become the guy.")
    elif a == 0:
        print("Oh, my keyboard!")
