import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline




def solve():
    nums = []
    for _ in range(3):
        nums.append(int(input()))
    ans = 0
    a , b , c = nums[0] , nums[1], nums[2]
    ans = max(ans, a + b + c, a + (b * c), (a * b) + c, (a + b) * c,a * (b + c), a * b * c )
    print(ans)
              



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
