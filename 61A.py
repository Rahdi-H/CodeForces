a = input("Enter: ")
b = input("Enter: ")

c = ""
for i in range(len(a)):
    if a[i] == b[i]:
        c += "0"
    else:
        c += "1"

print(c)
