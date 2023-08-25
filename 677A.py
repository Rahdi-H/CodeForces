n = input().split(" ")
o = input().split(" ")
w = 0
for i in o:
    if int(i) > int(n[1]):
        w += 2
    else:
        w += 1

print(w)
