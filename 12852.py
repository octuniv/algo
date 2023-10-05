import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
q = deque()
q.append(N)
while q:
    p = q.popleft()
    if p == 1: break
    if p % 3 == 0:
        np = p // 3
        if dp[np] == 0:
            dp[np] = p
            q.append(np)
    if p % 2 == 0:
        np = p // 2
        if dp[np] == 0:
            dp[np] = p
            q.append(np)
    np = p - 1
    if dp[np] == 0:
        dp[np] = p
        q.append(np)

ans = [1]
while True:
    p = ans[-1]
    t = dp[p]
    ans.append(t)
    if t == N: break
ans.reverse()
print(len(ans) - 1)
print(*ans, sep=' ')