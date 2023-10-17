n = int(input("Enter: "))
f = "h"
s = ""
for i in range(n):
    if f == "h":
        s += "I hate that "
        f = "l"
    else:
        s += "I love that "
        f = "h"
    if i+1 == n:
        s = s[:-5]
        s += "it"
    
print(s)
