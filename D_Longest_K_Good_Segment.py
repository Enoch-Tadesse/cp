from collections import defaultdict

n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))

seen = defaultdict(int)
l, r = -1, -1

left = 0
res = -1
for right in range(n):
    seen[nums[right]] += 1
    while len(seen) > m:
        seen[nums[left]] -= 1
        if seen[nums[left]] == 0:
            del seen[nums[left]]
        left += 1
    if right - left + 1 > res:
        l, r = left, right
        res = right - left + 1
print(l + 1, r + 1)
