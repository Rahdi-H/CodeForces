n, m = map(int, input("Enter: ").split(" "))
i = 0
while n >= 1 and m >= 1:
    n -= 1
    m -= 1
    i += 1
if i % 2 == 0:
    print("Malvika")
else:
    print("Akshat")
