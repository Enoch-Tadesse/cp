from collections import defaultdict
import random

t = int(input())
for _ in range(t):
    n, target = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    l = 0
    counter = 0
    seen = defaultdict(int)
    x = random.randint(1, 1000000)
    for r in range(len(nums)):
        find = (target - nums[r]) ^ x
        if find in seen and seen[find] > 0:
            counter += 1
            seen[find] -= 1
            continue
        seen[nums[r] ^ x] += 1
    print(counter)
