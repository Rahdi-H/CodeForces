a = input('Enter: ')
b = input('Enter: ')
if a.lower() < b.lower():
    print("-1")
elif b.lower() < a.lower():
    print("1")
else:
    print(0)
