t = int(input())

for _ in range(t):
    nums = [int(x) for x in input().strip()]
    left = nums[0]
    if left == 0:
        print(-1)
        continue
    i = 1
    while i < len(nums) and nums[i] == 0:
        left *= 10
        i += 1
    right = 0
    while i < len(nums):
        right *= 10
        right += nums[i]
        i += 1
    if left < right:
        print(left, right)
    else:
        print(-1)

