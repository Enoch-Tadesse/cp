import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy

input = sys.stdin.read

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

pre1 = [0] * (n + 1)
for i in range(n):
    pre1[i + 1] = pre1[i] + nums[i]

nums.sort()
pre2 = [0] * (n + 1)
for i in range(n):
    pre2[i + 1] = pre2[i] + nums[i]

q = int(sys.stdin.readline())

for _ in range(q):
    t, left, right = list(map(int, sys.stdin.readline().split()))
    if t == 1:
        print(pre1[right] - pre1[left - 1])
    else:
        print(pre2[right] - pre2[left - 1])
