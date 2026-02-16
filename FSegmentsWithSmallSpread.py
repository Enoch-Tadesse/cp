from collections import deque

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

counter = 0

_max = deque([])
_min = deque([])

left = 0
for right in range(n):
    while _max and nums[_max[-1]] < nums[right]:
        _max.pop()
    while _min and nums[_min[-1]] > nums[right]:
        _min.pop()
    _max.append(right)
    _min.append(right)
    if _max[0] < left:
        _max.popleft()
    if _min[0] < left:
        _min.popleft()
    while nums[_max[0]] - nums[_min[0]] > k:
        left += 1
        if _max[0] < left:
            _max.popleft()
        if _min[0] < left:
            _min.popleft()

    counter += right - left + 1
print(counter)
