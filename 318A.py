n = input("Enter: ").split(" ")
h = 0
if int(n[0]) % 2 == 0:
    h = int(n[0])/2
else:
    h = int(n[0])//2 + 1
if int(n[1]) <= int(n[0]):
    if int(n[1]) <= h:
        print(1 + (int(n[1])-1)*2)
    else:
        print(int(abs(2 + ((h - int(n[1]))-1)*2)))
