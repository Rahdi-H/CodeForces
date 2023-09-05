n = input("Enter: ").split("WUB")
s = ""
c = 0
for i in n:
    if i != "":
        if c == 0:
            s += i
            c += 1
        else:
            s += f" {i}"
            c += 1
print(s)
