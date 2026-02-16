# **
# >*
# *<
# ><


# <<<<<<*>>>>>>
# *>>>>>
# <<<<<*
# <<<<<<>>>>>>

t = int(input())

for _ in range(t):
    s = input().strip()
    if len(s) == 1:
        print(1)
        continue
    if "**" in s or ">*" in s or "*<" in s or "><" in s:
        print(-1)
    else:
        left = s.count("<")
        right = s.count(">")
        ask = s.count("*")
        print(max(left , right ) + ask)


