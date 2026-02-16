n, t = list(map(int, input().split()))

nums = list(map(int, input().split()))

out = float("-inf")
curr = 0
l = 0
for r in range(n):
    curr += nums[r]
    while curr > t:
        curr -= nums[l]
        l += 1
    out = max(out, r - l + 1)
print(out)
