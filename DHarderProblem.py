from random import randint

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    seen = set()
    x = randint(1, 1000000)

    output = []
    k = 0
    for num in nums:
        if num ^ x in seen:
            k += 1
            output.append("")
        else:
            output.append(num)
            seen.add(num ^ x)
    add = 1
    for i in range(len(output)):
        if output[i] == "":
            if k > 0:
                while add ^ x in seen:
                    add += 1
                k -= 1
                output[i] = add
                seen.add(add ^ x)
    print(*output)
