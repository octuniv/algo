import sys
input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]
dp = [0 for _ in range(N)]
LIS = [[] for _ in range(N)]

for i in range(N):
    dp[i] = 1
    LIS[i].append(arr[i])
    for j in range(0, i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            LIS[i] = [*LIS[j]]
            LIS[i].append(arr[i])
            dp[i] = dp[j] + 1

ind = 0
for i in range(1,N):
    if dp[ind] < dp[i]:
        ind = i

print(dp[ind])
print(*LIS[ind], sep=' ')