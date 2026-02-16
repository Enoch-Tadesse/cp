t = int(input())

for _ in range(t):
    s = input().strip()
    t = input().strip()
    p = input().strip()

    i = 0 # this points to s
    j = 0 # this points to t

    need = dict()

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            need[t[j]] = need.get(t[j], 0) + 1
            j += 1

    if i != len(s):
        print("NO")
        continue

    while j < len(t):
        need[t[j]] = need.get(t[j], 0) + 1
        j += 1

    
    have = dict()
    for e in p:
        have[e] = have.get(e, 0) + 1

    for ele , freq in need.items():
        if ele not in have:
            print("NO")
            break
        if freq > have[ele]:
            print("NO")
            break
    else:
        print("YES")


