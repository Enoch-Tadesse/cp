import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math
from random import randint

# input = input
input = sys.stdin.readline
big = randint(1, 10**9)


def solve():
    n, z = list(map(int, input().split()))
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    nums1 = list(map(lambda x: (x % z) ^ big, nums1))
    nums2 = list(map(lambda x: (x % z) ^ big, nums2))
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    it = [(k, v) for k, v in count1.items()]
    for k, v in it:
        for _ in range(v):
            count1[k] -= 1
            mod_val = k ^ big
            if count2[k]:
                count2[k] -= 1
            elif count2[((z - mod_val) % z) ^ big]:
                count2[((z - mod_val) % z) ^ big] -= 1
            else:
                print("NO")
                return
        if count1[k] == 0:
            del count1[k]
    print("YES" if len(count1) == 0 else "NO")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
