n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

queries = list(map(int, input().split()))

for q in queries:
    _max = -1
    l = 0
    r = n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] <= q:
            _max = mid + 1
            l = mid + 1
        else:
            r = mid - 1
    print(_max)
