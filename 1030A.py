n = int(input("Enter: "))
j = input("ENter: ")
c = 0
for i in j:
    if i != " ":
        c += int(i)

if c > 0:
    print("HARD")
else:
    print("EASY")
