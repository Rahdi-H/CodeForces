o = int(input())
m = 0
mx = 0
for i in range(o):
    n = input().split(" ")
    ex = int(n[0])
    en = int(n[1])
    m -= ex
    m += en
    if mx < m:
        mx = m

print(mx)
