l = int(input())
n = input()
zero = 0
one = 0
for i in n:
    if i == "0":
        zero += 1
    else:
        one += 1
 
if zero > one:
    print(zero - one)
else:
    print(one - zero)