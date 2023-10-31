t = int(input("Enter: "))
n = list(map(int, input("Enter: ").split()))

p = 0
c = 0
for i in n:
    if i == -1:
        if p >= 1:
            p -= 1
        else:
            c += 1
    else:
        p += i

print(c)
