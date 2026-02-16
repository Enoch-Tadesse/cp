s = input()
t = input()

ns = len(s)
nt = len(t)

if ns != nt:
    print("NO")
    exit()
i = 0
while i < ns:
    if s[i] != t[ns - i - 1]:
        print("NO")
        exit()
    i += 1
print("YES")
