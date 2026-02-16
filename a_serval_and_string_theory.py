import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def solve():
	n, k = list(map(int, input().split()))
	s = input().strip()
	if s < s[::-1] or (k >= 1 and min(s) != max(s)):
		print('YES')
	else:
		print('NO')
def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
