num = int(input())
counter = 0
while num > 0:
    check = num % 10
    if check == 4 or check == 7:
        counter += 1

    num //= 10
if counter == 4 or counter == 7:
    print("YES")
else:
    print("NO")
