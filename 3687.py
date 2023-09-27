from functools import reduce
import sys
input = sys.stdin.readline

match = [0,0,1,7,4,2,0,8,10]
dp = [0,0,1,7,4,2,6,8,10]

for i in range(9, 101):
    dp.append(min([dp[i - j] * 10 + match[j] for j in range(2, 8)]))
def sol_max(x):
    p = x // 2
    arr = [1 for _ in range(p)]
    if x % 2:
        arr[0] = 7
    return reduce(lambda acc, cur: acc * 10 + cur, arr, 0)

def sol_min(x):
    return dp[x]

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    ans.append([sol_min(N), sol_max(N)])
    
for a in ans:
    print(*a, sep=' ')