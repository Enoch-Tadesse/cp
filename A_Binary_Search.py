import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right

input = sys.stdin.read


n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
queries = list(map(int, input().split()))

for q in queries:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < q:
            l = mid + 1
        elif nums[mid] > q:
            r = mid - 1
        else:
            print("YES")
            break
    else:
        print("NO")
