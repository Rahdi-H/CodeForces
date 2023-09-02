n = int(input("Enter: "))
c = 0
p = ""
for _ in range(n):
    i = input("Enter: ")
    if p != i:
        c += 1
        p = i

print(c)
