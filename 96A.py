n = input("Enter: ")
c1 = 0
c0 = 0
for i in n:
    if i == "1":
        c0 = 0
        c1 += 1
    else:
        c1 = 0
        c0 += 1
    if c1 >= 7 or c0 >= 7:
        print("YES")
        break
if c0 < 7 and c1 < 7:
    print("NO")
