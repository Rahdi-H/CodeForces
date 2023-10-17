n = input("Enter: ")
if len(n) == 2:
    print(0)
else:
    i = set(n[1:-1].split(", "))
    print(len(i))
