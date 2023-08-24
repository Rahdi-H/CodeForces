s = input("Enter: ").split(" ")
q = input("Enter: ")
for i in range(int(s[1])):
    q = q.replace('BG', "GB")
print(q)
