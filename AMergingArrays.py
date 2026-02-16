n, m = list(map(int, input().split()))

left = list(map(int, input().split()))

right = list(map(int, input().split()))

l = 0
r = 0
output = []

while l < n and r < m:
    if left[l] <= right[r]:
        output.append(left[l])
        l += 1
    else:
        output.append(right[r])
        r += 1
if r < m:
    output.extend(right[r:])
if l < n:
    output.extend(left[l:])

print(*output)
