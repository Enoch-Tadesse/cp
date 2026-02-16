import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


counter = 0


def clean_up(nums):
    count = 0
    seen = defaultdict(int)
    for num in nums:
        count += seen[num + 1]
        seen[num] += 1
    return count


def merge(nums1, sum1, nums2, sum2):
    global counter
    i, j = 0, 0
    new_sum = sum1 + sum2
    cur1, cur2 = 0, 0  # sum of elements form nums1, nums2 that we processed
    new_array = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            # how many numbers are left from nums2 array
            left2 = len(nums2) - j
            # compete the current number to be removed with the numbers to be processed from nums2
            # sum2 - cur2 means the sum of numbers from nums2 that we have not processed yet
            toadd = sum2 - cur2 - left2 * nums1[i]
            counter += toadd
            cur1 += nums1[i]
            new_array.append(nums1[i])
            i += 1
        else:
            left1 = len(nums1) - i
            toadd = sum1 - cur1 - left1 * nums2[j]
            counter += -1 * toadd
            cur2 += nums2[j]
            new_array.append(nums2[j])
            j += 1
    new_array.extend(nums1[i:])
    new_array.extend(nums2[j:])
    return (new_array, new_sum)


def merge_sort(nums):
    if len(nums) <= 1:
        return (nums, sum(nums))
    mid = len(nums) // 2
    a1, s1 = merge_sort(nums[:mid])
    a2, s2 = merge_sort(nums[mid:])
    return merge(a1, s1, a2, s2)


def solve():
    global counter
    n = int(input())
    nums = list(map(int, input().split()))
    merge_sort(nums)
    counter += clean_up(nums)
    counter -= clean_up(nums[::-1])
    print(counter)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
