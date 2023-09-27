import sys
input = sys.stdin.readline

T = 3
ans = []

while T:
    T -= 1
    N = int(input())
    coin = []
    dp = [0 for _ in range(50001)]
    sum_val = 0
    for _ in range(N):
        t, c = map(int, input().split())
        coin.append([t, c])
        sum_val += t * c

    if sum_val % 2: 
        ans.append(0)
        continue
    
    dp[0] = 1
    
    for i in range(N):
        for j in range(50000, coin[i][0] - 1, -1):
            if dp[j - coin[i][0]] :
                for k in range(coin[i][1] + 1):
                    if j + k * coin[i][0] > 50000: break
                    dp[j + k * coin[i][0]] = 1
    
    ans.append(dp[sum_val // 2])
print(*ans, sep='\n')