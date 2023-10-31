t = int(input("Enter: "))
for _ in range(t):
    n = int(input("Enter: "))
    for pw in range(2, 30):
        val = (1 << pw) - 1
        if n % val == 0:
            print(n // val)
            break
