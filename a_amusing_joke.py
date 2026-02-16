import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    boss = ""
    words = ""
    boss += input().strip()
    boss += input().strip()
    boss = Counter(boss)
    words += input().strip()
    mini = Counter(words)
    for k , v in boss.items():
        if k not in mini or abs(v - mini[k]) > 0:
            print("NO")
            return
    print("YES")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
