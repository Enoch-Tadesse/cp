from collections import defaultdict

t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort()
    counts = defaultdict(int)
    right = 0
    while right < n:
        curr = nums[right]
        while (
            right < n - 1
            and nums[right] != nums[right - 1]
            and counts[nums] < k
        ):

