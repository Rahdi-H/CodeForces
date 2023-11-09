l = int(input("Enter: "))
n = input("Enter: ")
s = []
for i in range(l-1):
    s.append(f"{n[i]}{n[i+1]}")
c = 0
ele = ""
for i in s:
    co = s.count(i)
    if c == 0:
        c = co
    if co >= c:
        c = co
        ele = i    
    

print(ele)