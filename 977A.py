o = input().split(" ")
n = int(o[0])
k = int(o[1])
while k > 0:
    if str(n)[-1] != "0":
        n -= 1
        k -= 1
    else:
        n = n/10
        n = int(n)
        k -= 1
print(n)
