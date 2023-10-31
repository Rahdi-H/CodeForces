n, m = list(map(int, input("Enter: ").split()))
t = 1
for i in range(1, n+1):
    if i % 2 != 0:
        print("#"*m)
    elif t == 1:
        print(("."*(m-1))+"#")
        t = 2
    elif t == 2:
        print("#"+("."*(m-1)))
        t = 1
