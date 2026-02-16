from collections import defaultdict


t = int(input())

for _ in range(t):
    r, c = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(r)]
    sums = defaultdict(int)
    sums2 = defaultdict(int)
    for nr in range(r):
        for nc in range(c):
            sums[nr + nc] += mat[nr][nc]
            sums2[nr - nc] += mat[nr][nc]
    output = -1
    for nr in range(r):
        for nc in range(c):
            # print(sums[nr + nc], sums[nr - nc], nr + nc, nr - nc)
            output = max(output, sums[nr + nc] + sums2[nr - nc] - mat[nr][nc])

    # print("-----")
    print(output)
