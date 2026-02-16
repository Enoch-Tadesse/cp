import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    px, py, qx, qy = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    dist = math.sqrt((qx - px) ** 2 + (qy - py) ** 2)
    arr.append(dist)
    arr.sort()

    if arr[-1] - sum(arr[:-1]) > 0:
        print("NO")
    else:
        print("YES"   4   │
   3   │   if arr[-1] - sum(arr[:-1]) > 0:
   2   │   │   print("NO")
   1   │   else:
  22   │   │   print("YES")
   1
   2
   3
   4   def main():
   5       t = int(input())
   6
   7       for _ in range(t):
   8       │   solve()
   9
  10
  11   if __name__ == "__main__":
  12       main()
  14      2   │   │   print("NO")
  13      1   │   else:
  12     22   │   │   print("YES")
  11     │1
  10     │2
   9     │3
   8     │4   def main():
   7     │5       t = int(input())
   6     │6
   5     │7       for _ in range(t):
   4     │8       │   solve()
   3     │9
   2     10
   1     11   if __name__ == "__main__":
  38     12       main())
   1
   2
   3
   4   def main():
   5       t = int(input())
   6
   7       for _ in range(t):
   8       │   solve()
   9
  10
  11   if __name__ == "__main__":
  12       main())



def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
