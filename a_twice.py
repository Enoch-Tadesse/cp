def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    seen = set()
    score = 0
    for num in nums:
        # you have seen this number twice
        # remove it and increment the score
        if num in seen:
            score += 1
            seen.remove(num)
        else:
            # put the number in seen, if you see it again
            # you will increment the score
            seen.add(num)
    print(score)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
