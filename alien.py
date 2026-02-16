import sys
#sys.setrecursionlimit(10**6)
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from copy import deepcopy
import math

# input = input
input = sys.stdin.readline


class Solution:
    def findOrder(self, words):
        n = len(words)
        all_chars = sorted(set(c for w in words for c in w))
        adj = defaultdict(lambda : [0, []])
        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]
            t , b = 0 , 0
            while t < len(word1) and b < len(word2):
                if word1[t] == word2[b]:
                    t , b = t + 1, b + 1
                    continue
                adj[word1[t]][1].append(word2[b])
                adj[word2[b]][0] += 1
                break
            else:
                if len(word1) > len(word2):
                    return ""
        for c in all_chars:
            adj[c]
        for k in list(adj.keys()):
            adj[k][1] = sorted(set(adj[k][1]))
        return self.valid(adj, all_chars)
    def valid(self, adj, all_chars):
        q = deque(c for c in all_chars if adj[c][0] == 0)
        visited = set()
        seq = []
        while q:
            curr = q.popleft()
            visited.add(curr)
            seq.append(curr)
            for nei in adj[curr][1]:
                adj[nei][0] -= 1
                if adj[nei][0] == 0:
                    q.append(nei)
        if len(visited) != len(all_chars):
            return ""
        return "".join(seq)


sol = Solution()
words = ["baa", "abcd", "abca", "cab", "cad"]
print(sol.findOrder(words))
