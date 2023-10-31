n = int(input("Enter: "))
s = list(map(int, input("Enter: ").split(" ")))

mx_i = 0
mn_i = 0
while (s[0] != max(s)) or (s[-1] != min(s)):
    if s[0] != max(s):
        mx = max(s)
        l = [mx]
        mx_i = s.index(mx)
        s.pop(mx_i)
        l.extend(s)
        s = l

    if s[-1] != min(s):
        s.reverse()
        mn = min(s)
        l = [mn]
        mn_i = s.index(mn)
        s.pop(mn_i)
        l.extend(s)
        s = l
        s.reverse()

print(mx_i + mn_i)
