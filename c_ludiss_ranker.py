n = int(input())

ratings = list(map(int, input().split()))

rank = [-1] * n

pairs = [(rating, i) for i, rating in enumerate(ratings)]

pairs.sort(reverse=True)

counter = 1

seen = {}

for rating, i in pairs:
    if rating in seen:
        rank[i] = seen[rating]
    else:
        rank[i] = counter
        seen[rating] = rank[i]
    counter += 1
print(*rank)


