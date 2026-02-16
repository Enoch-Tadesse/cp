def left_close(target, nums):
    # returns max index closing in from the left
    l = 0
    r = len(nums) - 1
    _max = -1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] <= target:
            _max = mid
            l = mid + 1
        else:
            r = mid - 1
    return _max


def right_close(target, nums):
    # returns the smallest index closing in from the right
    l = 0
    r = len(nums) - 1
    _min = -1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            _min = mid
            r = mid - 1
    return _min


n = int(input())
nums = list(map(int, input().split()))
nums.sort()

r = int(input())
queries = [list(map(int, input().split())) for _ in range(r)]


for left, right in queries:
    right_val = left_close(right, nums)
    left_val = right_close(left, nums)
    if left_val == -1 or right_val == -1:
        print(0, end=" ")
    else:
        print(right_val - left_val + 1, end=" ")
