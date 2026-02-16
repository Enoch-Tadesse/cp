import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    nums = list(x for x in input().strip())
    counts = Counter(nums)
    cnt = [[i, freq] for i, freq in counts.items()]
    cnt.sort(reverse=True)
    for i in range(len(cnt)):
        if cnt[i][0] == "0":
            continue
        cnt[i][1] -= 1
        print(cnt[i][0], end="")
    for i in range(len(cnt) - 1, -1, -1):
        if cnt[i][0] == "0":
            continue
        print(cnt[i][0] * cnt[i][1], end="")
    print("0" * counts["0"])


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
