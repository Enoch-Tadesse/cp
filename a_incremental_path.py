import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        s = input().strip()
        blacks = list(map(int, input().split()))

        # Track the relative range of movement
        pos = 0
        min_pos = max_pos = 0

        for c in s:
            if c == 'A':
                pos += 1
            else:  # 'B'
                pos += 1
            min_pos = min(min_pos, pos)
            max_pos = max(max_pos, pos)

        # All positions between [1 + min_pos, 1 + max_pos] become black
        start = 1 + min_pos
        end = 1 + max_pos

        # Merge initial and new black cells
        final_blacks = set(blacks)
        for x in range(start, end + 1):
            final_blacks.add(x)

        final_sorted = sorted(final_blacks)
        print(len(final_sorted))
        print(*final_sorted)
solve()
