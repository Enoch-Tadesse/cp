from collections import defaultdict, Counter
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    string = input().strip()
    pres = defaultdict(list)
    counts = Counter(string)
    for i in range(0, 26):
        c = chr(ord("a") + i)
        run = 0
        for char in string:
            run += char == c
            pres[c].append(run)
    for _ in range(q):
        left, right, char = map(str, input().split())
        left = int(left)
        left -= 1
        right = int(right)
        dec = counts[char] * ((left - 1) // n)
        inc = counts[char] * ((right - 1) // n)

        # print(f"{inc=} {dec=}")

        left = (left - 1) % n
        right = (right - 1) % n

        dec += pres[char][left]
        inc += pres[char][right]

        print(inc - dec)
