h, w, n = list(map(int, input().split()))
l = 1
r = max(h, w) * max(h, w) * n


def can(w, h, n, m):
    up = m // h
    side = m // w
    return up * side >= n


# ans = -1
while l <= r:
    mid = l + (r - l) // 2
    if can(w, h, n, mid):
        r = mid - 1
        # ans = mid
    else:
        l = mid + 1
print(l)
