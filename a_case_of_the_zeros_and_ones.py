n = int(input())

nums = input()

ones = 0
zeros = 0

for num in nums:
    if num == "1":
        ones += 1
    else:
        zeros += 1

print(abs(ones - zeros))

