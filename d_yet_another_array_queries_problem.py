def solve():
    n, q, m = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    queries.reverse()
    # reverse the queries for simulation

    find = list(map(int, input().split()))

    for i in range(m):
        now = find[i] - 1  # adjust the current index to 0 indexed
        for t, l, r in queries:
            l -= 1  # adjust indexes to 0 indexed
            r -= 1

            # if the query does not affect the current index we are in, ignore it
            if not (l <= now <= r):
                continue

            # the query is for right shift, since we are doing in reverse
            # we will do left shift instead
            if t == 1:
                # move it back to r
                if now == l:
                    now = r
                # otherwise just decrement the now index
                else:
                    now -= 1
            else:
                # rotate it, just basic math
                now = l + r - now
        print(nums[now])


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
