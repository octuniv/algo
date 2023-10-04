import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
inp = []
for _ in range(N):
    A, B = map(int, input().split())
    inp.append([A, B])

temp = 0
for i in range(N):
    t, p = inp[i]
    temp = max(temp, dp[i])
    if i + t > N: continue
    dp[i+t] = max(dp[i+t], temp + p)
print(max(dp))