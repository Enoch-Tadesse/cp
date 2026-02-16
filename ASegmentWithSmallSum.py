n, target = list(map(int, input().split()))

nums = list(map(int, input().split()))

curr = 0
_max = 0
l = 0
for r in range(n):
    curr += nums[r]
    while curr > target:
        curr -= nums[l]
        l += 1
    _max = max(_max, r - l + 1)
print(_max)
