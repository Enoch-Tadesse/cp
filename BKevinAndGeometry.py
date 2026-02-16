t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    n = len(nums)
    output = []
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            output.extend([nums[i - 1], nums[i]])
            nums.pop(i - 1)
            nums.pop(i - 1)
            n -= 2
            break
    else:
        print(-1)
        continue
    for i in range(n - 1):
        if nums[i + 1] - nums[i] < 2 * output[0]:
            print(*output, nums[i], nums[i + 1])
            break
    else:
        print(-1)
        continue
