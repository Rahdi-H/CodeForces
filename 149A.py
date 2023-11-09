l = int(input("Enter: "))
n = list(map(int, input("Enter: ").split(" ")))
n.sort(reverse=True)
c = 0
s = 0
while s < l and c <= 11:
    s += n[c]
    c += 1
 
if s >= l:
    print(c)
else:
    print(-1)