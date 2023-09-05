n = int(input("Enter: "))
if n > -1:
    print(n)
else:
    s = list(str(n))
    del s[-1]
    s1 = int("".join(s))
    s = list(str(n))
    del s[-2]
    s2 = int("".join(s))
    if s1 > s2:
        if abs(s1) == 0:
            print(abs(s1))
        else:
            print(s1)
    else:
        if abs(s2) == 0:
            print(abs(s2))
        else:
            print(s2)
