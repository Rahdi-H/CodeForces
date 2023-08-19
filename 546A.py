n = input("Enter: ").split(" ")
k = int(n[0])
j = int(n[1])
w = int(n[2]) + 1
t = 0
for i in range(1, w):
    t += i * k

if t > j:
    print(t - j)
else:
    print(0)
