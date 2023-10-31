n = int(input("Enter: "))
s = input("Enter: ")

alpha = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if n < 26:
    print("NO")
else:
    for i in s:
        if alpha.count(i.lower()):
            alpha.remove(i.lower())
    if len(alpha) == 0:
        print("YES")
    else:
        print("NO")
