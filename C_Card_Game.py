################# observation #########################

# player with both 1 and n card can win everytime
# case 2 :
# player of 1 and n differs
# case 2.1 :
# if bob got only n, he lost
# else alice lost
# case 2.2 :
# if bob is with number one, interesting
# if alice got no other thing than n, she loses
# but there is a chance for her to win
# who ever got the next biggest number wins

import sys
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


def solve():
    n = int(input())
    cards = list(x for x in input().strip())
    if n == 2:
        if cards[0] == "A":
            print("Alice")
            return
        else:
            print("Bob")
            return
    counts = defaultdict(set)
    for i, card in enumerate(cards):
        counts[card].add(i + 1)
    if cards[0] == cards[n - 1]:
        if cards[0] == "A":
            print("Alice")
            return
        else:
            print("Bob")
            return
    if cards[n - 1] == "B":
        if len(counts["B"]) == 1:
            print("Alice")
            return
        else:
            print("Bob")
            return
    if cards[0] == "B":
        if len(counts["A"]) == 1:
            print("Bob")
            return
        counts["A"].discard(n)
        a_got = max(counts["A"])
        b_got = max(counts["B"])
        if a_got > b_got:
            print("Alice")
            return
        else:
            print("Bob")
            return


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
