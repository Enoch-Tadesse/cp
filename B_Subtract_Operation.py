import sys
from random import randint
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy

input = sys.stdin.read


t = int(sys.stdin.readline())
for _ in range(t):
    n, k = list(map(int, sys.stdin.readline().split()))
    nums = list(map(int, sys.stdin.readline().split()))

    nums.sort()
    x = randint(1, 1_000_000)
    seen = set()
    # seen.add(0 ^ x)

    for num in nums:
        if (num - k) ^ x in seen:
            print("YES")
            break
        seen.add(num ^ x)
    else:
        print("NO")
