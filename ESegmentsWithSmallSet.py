from collections import defaultdict

n, k = list(map(int, input().split()))

nums = list(map(int, input().split()))

seen = defaultdict(int)

counter = 0
left = 0

for right in range(n):
    seen[nums[right]] += 1
    while len(seen) > k:
        seen[nums[left]] -= 1
        if seen[nums[left]] == 0:
            del seen[nums[left]]
        left += 1
    counter += right - left + 1
print(counter)
