n = int(input("Enter: "))
l = input()
p = l[0]
c = 0
for i in range(1, n):
    if l[i] == p:
        c += 1
        p = l[i]
    else:
        p = l[i]

print(c)
