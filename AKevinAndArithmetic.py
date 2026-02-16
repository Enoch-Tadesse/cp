t = int(input())

for _ in range(t):
    n = int(input())

    nums = list(map(int, input().split()))

    evens = 0
    for num in nums:
        if num % 2 == 0:
            evens += 1
    odds = n - evens
    if evens > 0:
        print(odds + 1)
        continue
    print(odds - 1)
