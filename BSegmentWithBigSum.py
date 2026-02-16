n, target = list(map(int, input().split()))

nums = list(map(int, input().split()))

res = float("inf")
curr = 0
left = 0
for right in range(n):
    curr += nums[right]
    while curr >= target:
        res = min(res, right - left + 1)
        curr -= nums[left]
        left += 1
print(-1 if res == float("inf") else res)
