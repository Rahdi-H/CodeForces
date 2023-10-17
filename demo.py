t = int(input("Enter: "))

for _ in range(t):
    a, b = list(map(int, input("Enter: ").split(" ")))
    c = 0
    if a < b:
        c = b-a
    elif a/2 > b:
        j = a % b
        c = b - j
    elif a == b:
        continue
    else:
        c = b * 2 - a
    print(c)
