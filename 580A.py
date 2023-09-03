n = input("Enter: ")
j = input("Ente: ").split(" ")
num = 0
pv = 0
pr = 0
for i in j:
    if int(i) >= num:
        pr += 1
        num = int(i)
    else:
        if pv < pr:
            pv = pr
        pr = 1
        num = int(i)
print(max(pv, pr))
