n = input('enter: ')
j = ""
c = 0
for i in n:
    if j.find(i) >= 0:
        continue
    else:
        c += 1
        j += i
if c % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
