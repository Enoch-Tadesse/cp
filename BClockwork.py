t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(n):
        if nums[i] - 2 * (n - i - 1) <= 0 or nums[i] - i * 2 <= 0:
            print("NO")
            break
    else:
        print("YES")
