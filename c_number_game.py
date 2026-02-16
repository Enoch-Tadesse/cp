import sys

# sys.setrecursionlimit(10**6)
from collections import *
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint
from math import *
from heapq import *

# input = input
input = sys.stdin.readline


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve():
    n = int(input())
    # whoever is on power of two losses
    # whoever has an odd number besides 1 wins,
    # just choose to divide the number by itself, and the next person will have 1
    # which makes them lose

    game = ["Ashishgup", "FastestFinger"]
    if n == 1: # whoever has this, loses
        print(game[1])
    elif n == 2:
        print(game[0])
    elif n == 3: # game[0] can divide 3 by itself, and get 1, then game[1] will lose
        print(game[0])
    else:
        if n.bit_count() == 1:
            # if the number is a power of two, there is no odd divisor
            # the only option is to do -1, then even number minus 1 will give an odd number
            # the next pweron will hold the odd number and divide it by itself
            # which makes the next person game[1] win the game
            print(game[1])
        elif n % 2 == 0 and is_prime(n // 2):
            # any number is made up of 2 ** k * m, meaning m is odd.
            # game[0] will try to lead the game[1] to have only 2 ** k
            # leaving him with a power of two, but if m is the only odd divisor
            # that means n = 2 * prime, he can only divide by the prime, and game[1]
            # will have 2, which he will subtract 1 and wins
            print(game[1])
        else:
            # other wise, game[0] will divide by m and will leave game[1] with
            # only 2 ** k, a power of two, and game[1] will lose
            print(game[0])


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
