n = input("ENter: ")
j = input("ENter: ").split(" ")
r = []
for i in range(len(j)):
    k = j.index(f"{i+1}")
    r.append(str(k+1))

print(" ".join(r))
