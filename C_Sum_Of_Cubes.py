import math
from random import randint

t = int(input())
for _ in range(t):

    n = int(input())
    x = randint(1, 1_000_000)
    run = 0
    seen = set()
    for i in range(1, math.ceil(math.cbrt(n))):
        seen.add((i**3) ^ x)
    for num in seen:
        if (n - (num ^ x)) ^ x in seen:
            print("YES")
            break
    else:
        print("NO")
