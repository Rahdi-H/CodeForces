n = input('enter: ').split("+")
n.sort()
j = ""
f = True
for i in n:
    if f:
        j += i
        f = False
    else:
        j += f"+{i}"
print(j)
