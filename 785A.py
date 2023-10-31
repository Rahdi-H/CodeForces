n = int(input("Enter: "))
f = 0
for _ in range(n):
    i = input("Enter: ")
    if i == "Tetrahedron":
        f += 4
    elif i == "Cube":
        f += 6
    elif i == "Octahedron":
        f += 8
    elif i == "Dodecahedron":
        f += 12
    elif i == "Icosahedron":
        f += 20

print(f)