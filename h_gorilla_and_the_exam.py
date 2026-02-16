from random import randint

big = randint(1000, 10**6)  # get the random number here

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x ^ big for x in a]  # randomize every number so you won't get hacked
    # after all what matters is the frequency no the actual numbers
    freq = {}
    for x in a:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    costs = []
    for count in freq.values():
        costs.append(count)
    costs.sort()
    elim = 0
    for c in costs:
        if k >= c:
            k -= c
            elim += 1
        else:
            break
    elim = min(elim, len(costs) - 1)
    print(len(costs) - elim)
