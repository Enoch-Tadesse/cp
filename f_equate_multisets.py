import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline

def reduce(num):
    while num & 1 == 0 and num > 1:
        num >>= 1
    return num

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(map(reduce, a))
    b = list(map(int, input().split()))
    cnt_a = Counter(a)
    b.sort()
    for i in range(n - 1, -1, -1):
        num = b[i]
        if num in cnt_a and cnt_a[num] > 0:
            cnt_a[num] -= 1
            if cnt_a[num] == 0:
                del cnt_a[num]
            continue
        while num > 0:
            look = num // 2
            if look in cnt_a:
                cnt_a[look] -= 1
                if cnt_a[look] == 0:
                    del cnt_a[look]
                break
            num = look
        else:
            print("NO")
            return
    print("YES")

    


def main():
    t = int(input())
    
    for _ in range(t):
        solve()


if __name__ == '__main__':
    main()
