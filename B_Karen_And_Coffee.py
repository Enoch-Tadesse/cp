n, k, q = list(map(int, input().split()))

pre = [0] * 200_002

for i in range(n):
    l, r = list(map(int, input().split()))
    pre[l] += 1
    pre[r + 1] -= 1

for i in range(1, len(pre)):
    pre[i] += pre[i - 1]

counts = [0] * 200_001
run = 0
for i in range(len(counts)):
    run += pre[i] >= k
    counts[i] += run
for i in range(q):
    l, r = list(map(int, input().split()))
    print(counts[r] - counts[l - 1])
