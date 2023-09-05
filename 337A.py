# Solution No. 1

# n, m = map(int, input(" enter: ").split(" "))
# f = list(map(int, input("Enter: ").split(" ")))

# f.sort()  # Sort the list in ascending order

# min_diff = float('inf')  # Initialize with a large value
# print(min_diff)
# for right in range(n, m + 1):
#     min_diff = min(min_diff, f[right - 1] - f[right - n])

# print(min_diff)

# Solution No. 2
n, m = map(int, input("Enter: ").split(" "))
p = list(map(int, input("Enter: ").split(" ")))
p.sort()
d = p[len(p)-1]
for i in range((m-n)+1):
    d = min(d, p[(i + n)-1] - p[i])

print(d)
