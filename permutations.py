def main():
    n = int(input())
    if n == 1:
        print(1)
    elif n <= 3:
        print("NO SOLUTION")
    elif n == 4: # edge case
        print(*[2, 4, 1, 3])
    else:
        evens, odds = [], []
        for i in range(1, n + 1):
            if i % 2 == 1:
                odds.append(i)
            else:
                evens.append(i)
        evens.reverse()
        odds.reverse()
        ans = evens + odds
        print(*ans)


if __name__ == "__main__":
    main()
