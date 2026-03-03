import sys
input = sys.stdin.readline

MAXA = 10**6 + 1
spf = [0] * MAXA

for i in range(2, MAXA):
    if spf[i] == 0:
        for j in range(i, MAXA, i):
            if spf[j] == 0:
                spf[j] = i

def omega(x):
    cnt = 0
    while x > 1:
        cnt += 1
        x //= spf[x]
    return cnt

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # if already non-decreasing → Bob
    if all(a[i] <= a[i+1] for i in range(n-1)):
        print("Bob")
        return

    moves = 0
    for x in a:
        moves += omega(x) - 1

    if moves % 2:
        print("Alice")
    else:
        print("Bob")

t = int(input())
for _ in range(t):
    solve()
