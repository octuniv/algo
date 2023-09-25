import sys
from collections import deque
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
stars = []
ans = 0

for _ in range(K):
    stars.append(list(map(int, input().split())))

for i in range(K):
    fx, _ = stars[i]
    for j in range(K):
        _, sy = stars[j]
        res = 0
        for t in range(K):
            tx, ty = stars[t]
            if fx <= tx and tx <= fx + L and sy <= ty and ty <= sy + L:
                res += 1
                ans = max(ans, res)
print(K - ans)