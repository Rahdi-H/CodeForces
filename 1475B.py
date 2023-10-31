t = int(input("Enter: "))
for _ in range(t):
    n = int(input("Enter: "))
    if n < 2020:
        print('NO')
    else:
        a = n % 2020
        b = (n - a) / 2020
        if b >= a:
            print("YES")
        else:
            print("NO")
