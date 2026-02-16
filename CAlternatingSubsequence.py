t = int(input())


def sign(num):
    if num < 0:
        return -1
    return 1


for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    output = 0
    right = 0
    while right < n:
        curr = nums[right]
        while right < n - 1 and sign(nums[right]) == sign(nums[right + 1]):
            curr = max(curr, nums[right + 1])
            right += 1
        output += curr
        right += 1
    print(output)
