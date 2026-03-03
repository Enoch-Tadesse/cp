from collections import Counter, defaultdict
from random import randint

t = int(input())


big = randint(1, 10**9)

for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))

    count = defaultdict(int)
    for num in d:
        count[num ^ big] += 1
    cards = sorted(count.keys(), key=lambda x: x ^ big)

    m, num_card, l = 0, 0, 0
    for r in range(len(cards)):
        num_card += count[cards[r]]

        while (r > l and r > 0) and (
            (cards[r] ^ big) - (cards[r - 1] ^ big) > 1 or r - l + 1 > k
        ):
            num_card -= count[cards[l]]
            l += 1
        m = max(m, num_card)

    print(m)
