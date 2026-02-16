n, k = list(map(int, input().split()))

nums = list(map(int, input().split()))

queries = list(map(int, input().split()))

for q in queries:
    l = 0
    r = n - 1

    _max = -1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < q:
            l = mid + 1
        else:
            _max = mid + 1
            r = mid - 1
    print(_max if _max != -1 else n + 1)
