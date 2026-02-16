n, m = list(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

output = []
left = 0
for r in range(m):
    while left < n and arr1[left] < arr2[r]:
        left += 1
    output.append(left)
print(*output)
