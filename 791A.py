n = input("Enter: ").split(" ")
l = int(n[0])
b = int(n[1])
y = 0
while (b >= l):
    b *= 2
    l *= 3
    y += 1

print(y)
