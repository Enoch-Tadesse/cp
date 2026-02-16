n = int(input())

nums = list(map(int, input().split()))

m = min(nums)

if nums.count(m) > 1:
    print("Still Rozdil")
else:
    print(nums.index(m) + 1)
