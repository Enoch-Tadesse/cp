t = int(input())

for _ in range(t):
    r, c = list(map(int, input().split()))
    nums = [list(map(int, input().split())) for _ in range(r)]
    nums = [list(x) for x in zip(*nums[::-1])]
    master = 0
    for num in nums:
        num.sort(reverse=True)
        pre = sum(num)
        counter = 0
        for i in range(r):
            pre -= num[i]
            counter += abs((r - i - 1) * num[i] - pre)
        master += counter
    print(master)
