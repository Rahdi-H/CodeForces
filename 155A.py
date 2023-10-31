t = int(input("Enter: "))
n = list(map(int, input("Enter: ").split()))
lt = n[0]
lb = n[0]
a = 0
for i in n:
    if i > lt:
        a += 1
        lt = i
    elif i < lb:
        a += 1
        lb = i

print(a)
