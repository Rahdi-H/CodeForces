n = int(input())
for i in range(0, n):
    a = str(input())
    if len(a) > 10:
        print(f"{a[0]}{len(a)-2}{a[-1]}")
    else:
        print(a)
