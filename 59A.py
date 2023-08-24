n = input()
l = len(n)
u = 0
for i in n:
    if i.isupper():
        u += 1

if u > l/2:
    print(n.upper())
else:
    print(n.lower())
