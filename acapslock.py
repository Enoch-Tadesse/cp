import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    word = input().strip()
    upper = ord('Z')
    lower = ord('A')
    for i in range(1, len(word)):
        cand = ord(word[i])
        if cand >= lower and cand <= upper:
            continue
        print(word)
        return
    for w in word:
        print(w.swapcase(), end = '')
    print()

        


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
