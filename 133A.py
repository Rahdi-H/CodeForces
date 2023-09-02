n = input('Enter: ')
c = "HQ9"
l = False
for i in n:
    for j in c:
        if j == i:
            l = True
            break
if l:
    print("YES")
else:
    print("NO")
