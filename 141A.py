a = list(input("Enter: "))
b = list(input("Enter: "))
f = list(input("Enter: "))
if len(f) != (len(a)+len(b)):
    print('NO')
else:
    for i in a:
        if i in f:
            ii = f.index(i)
            f.pop(ii)
    for i in b:
        if i in f:
            ii = f.index(i)
            f.pop(ii)

    if len(f) == 0:
        print("YES")
    else:
        print("NO")
