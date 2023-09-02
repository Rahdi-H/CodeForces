n = input("Enter: ")
c = input("Enter: ").split(" ")
k = list(map(int, c))
k.sort(reverse=True)
s = 0
for i in k:
    s += i
o = 0
for i, v in enumerate(k):
    if v+o > s-(v+o):
        print(i+1)
        break
    else:
        o += v
