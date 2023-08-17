n = int(input())
x = 0
for _ in range(0, n):
    i = input()
    if i.upper() == "X++" or i.upper() == "++X":
        x += 1
    else:
        x -= 1

print(x)
