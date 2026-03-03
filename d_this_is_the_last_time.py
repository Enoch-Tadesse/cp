t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    casino = []

    for _ in range(n):
        casino.append(list(map(int, input().split())))

    casino.sort()

    for i in range(n):
        l, r, real = casino[i]

        if l <= k <= r and real > k:
            k = real

    print(k)
