n = int(input())
p = 0
for i in range(n):
    a = input()
    if a.count("1") >= 2:
        p += 1

print(p)
