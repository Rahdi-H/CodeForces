# t = int(input("Enter: "))
# l = ["NO" for _ in range(t)]
# for i in range(t):
#     n = int(input('Enter: '))
#     for j in range(1, n+1, 2):
#         if j > 1 and n % j == 0 and l[i] == "NO":
#             l[i] = 'YES'
#             break

# for i in l:
#     print(i)

import math

# Function to check if n has an odd divisor greater than one


def has_odd_divisor(n):
    if n % 2 == 1:
        return True  # n itself is an odd divisor
    while n % 2 == 0:
        n //= 2  # Divide n by 2 until it's odd
    if n > 1:
        return True
    return False


# Number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    if has_odd_divisor(n):
        print("YES")
    else:
        print("NO")
