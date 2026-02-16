n, target = list(map(int, input().split()))
nums = list(map(int, input().split()))
curr = 0
res = 0
left = 0
for right in range(n):
    curr += nums[right]
    while curr >= target:  # at least
        res += n - right
        curr -= nums[left]
        left += 1
print(res)
