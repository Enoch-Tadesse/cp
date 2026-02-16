import math


n, k = map(int, input().split())

oddStop = math.ceil(n / 2)
isodd = k <= oddStop

if isodd:
    print(1 + (k - 1) * 2)
else:
    print(0 + (k - oddStop) * 2)
