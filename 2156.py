import sys
input = sys.stdin.readline

N = int(input())
alc = []
for _ in range(N):
    alc.append(int(input()))

dp = [alc[0]]

if N >= 2:
    dp.append(alc[0] + alc[1])

if N >= 3:
    dp.append(max(alc[0] + alc[1] , alc[1] + alc[2], alc[0] + alc[2]))

for i in range(3, N):
    dp.append(max(dp[-1], alc[i] + alc[i-1] + dp[i-3], alc[i] + dp[i-2]))
print(max(dp))