n = input().split(" ")
count = 0
i = input()
k = i.split(" ")
for j in k:
    if int(j) and int(k[int(n[1]) - 1]) <= int(j):
        count += 1

print(count)
