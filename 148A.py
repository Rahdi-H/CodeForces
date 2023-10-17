k = int(input("Enter; "))
l = int(input("Enter; "))
m = int(input("Enter; "))
n = int(input("Enter; "))
d = int(input("Enter; "))

dmg = 0

for i in range(1, d+1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        dmg += 1

print(dmg)
