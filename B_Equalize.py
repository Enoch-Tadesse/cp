t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    out = [nums[0]]
    for i in range(1, n):
        if nums[i] != out[-1]:
            out.append(nums[i])

    res = -1
    l = 0
    for r in range(len(out)):
        while out[r] - out[l] > n - 1:
            l += 1
        res = max(res, r - l + 1)
    print(res)
