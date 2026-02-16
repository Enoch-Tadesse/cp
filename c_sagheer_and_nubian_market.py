import sys

# sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
import heapq
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def can(nums, s, t):
    if t == 0:
        return float("inf")
    costs = [] # max heap
    total = 0 # total cost
    for i in range(len(nums)):
        cost, idx = nums[i], i + 1
        pay = cost + idx * (t)
        if total + pay > s or len(costs) >= t:
            if not costs or -1 * costs[0] <= pay:
                continue
            total += heapq.heappop(costs)
        total += pay
        heapq.heappush(costs, -1 * pay)
    if len(costs) == t: # he has to buy all the items
        return total
    return 0


def solve():
    n, s = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    l , r = 0 , 10 ** 9 + 1
    exp = float("inf") # expenditure
    count = 0 # how many he can buy
    while l <= r:
        mid = l + (r - l) // 2
        total = can(nums, s, mid)
        if total > 0:
            if mid > count:
                count = mid
                exp = total
            elif mid == count:
                exp = min(total , exp)
            l = mid + 1
        else:
            r = mid - 1
    if exp == float("inf") or r == 0:
        print(0 , 0)
        return
    print(count, exp)



def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
