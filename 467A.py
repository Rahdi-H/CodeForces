n = int(input("Enter: "))
c = 0
for _ in range(n):
    i = input("Enter: ").split(" ")
    if (int(i[1]) - int(i[0])) >= 2:
        c += 1

print(c)
