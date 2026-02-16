n, target = list(map(int, input().split()))

nums = list(map(int, input().split()))

output = 0
curr = 0
left = 0
for right in range(len(nums)):
    curr += nums[right]
    while curr > target:
        curr -= nums[left]
        left += 1
    output += right - left + 1
print(output)
