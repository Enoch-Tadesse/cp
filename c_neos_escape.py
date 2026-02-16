import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    # this is the start
    temp = []
    last = -1
    f = 0
    for num in nums:
        if num == last:
            f += 1
        else:
            f = 1
            last = num
        if f <= 1:
            temp.append(num)
    nums = temp
    n = len(nums)
    # this is the end

    pair = [(num, i) for i, num in enumerate(nums)]
    pair.sort(reverse=True)
    counter = 0
    seen = set()
    for num, i in pair:
        if i in seen or i - 1 in seen or i + 1 in seen:
            seen.add(i)
            continue
        seen.add(i)
        j = i - 1
        while j > 0 and nums[j] > nums[i]:
            seen.add(j)
            j -= 1
        j = i + 1
        while j < n and nums[j] > nums[i]:
            seen.add(j)
            j += 1
        counter += 1
    print(counter)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
