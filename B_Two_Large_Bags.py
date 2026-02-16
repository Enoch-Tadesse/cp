from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    counter = Counter(nums)
    _max = max(list(counter.keys()))
    print(nums)
    for i in range(_max, 0, -1):
        print(f"before change {counter=}")
        if counter[i] >= 0 and counter[i] % 2 == 0:
            print(counter)
            continue
        elif counter[i] < 0:
            counter[i - 1] += counter[i] * 3
            print(f"neg {counter=}")
        else:
            counter[i - 1] = -3 + counter.get(i - 1, 0)
            print(f"odd {counter=}")
    if counter[1] >= 0 and counter[1] % 2 == 0:
        print("Yes")
    else:
        print("No")
    print("-----case", _ + 2, "-------")
