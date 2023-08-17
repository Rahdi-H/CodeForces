n = input().split(" ")
b = int(n[0]) * int(n[1])
p = 0
while (b >= 2):
    p += 1
    b -= 2
print(p)
