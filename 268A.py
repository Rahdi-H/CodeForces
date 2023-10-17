n = int(input("Enter: "))
l = [

]
c = 0
for i in range(n):
    j = list(map(int, input("Ente: ").split(" ")))
    l.append(j)

for i in l:
    j = i[0]
    for k in l:
        if j == k[1]:
            c += 1

print(c)
