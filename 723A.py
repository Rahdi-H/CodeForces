n = list(map(int, input("Enter: ").split(" ")))
n.sort()
print(n[len(n)-1] - n[0])
