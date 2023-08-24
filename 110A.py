o = input()
l = len(o)
c = 0
for i in o:
    if i == "4" or i == "7":
        c += 1

if (c == 4 or c == 7):
    print("YES")
else:
    print("NO")
