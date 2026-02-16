import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy

input = input


def solve():
    s = input().strip()
    stack = []
    for string in s:
        if stack and stack[-1] == string:
            while stack and stack[-1] == string:
                stack.pop()
        else:
            stack.append(string)
    print("Yes" if len(stack) == 0 else "No")


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
