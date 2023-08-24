o = int(input())
n = input()
a = 0
d = 0
for i in range(o):
    if n[i] == "A":
        a += 1
    elif n[i] == "D":
        d += 1

if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")
