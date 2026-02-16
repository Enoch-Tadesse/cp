from collections import defaultdict


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    if n < 3:
        print(-1)
        continue
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
        if counts[num] == 3:
            print(num)
            break
    else:
        print(-1)
