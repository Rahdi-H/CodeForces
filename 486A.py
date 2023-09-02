n = int(input("Enter: "))
if n % 2 == 0:
    print(int(n/2))
else:
    n = (n-1)/2
    print(int(-(n+1)))
