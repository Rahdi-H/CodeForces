n = input("Enter: ")
j = input("Enter: ").split(" ")
a = 0
for i in j:
    a += int(i)

print(a/len(j))
