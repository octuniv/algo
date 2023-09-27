import sys
input = sys.stdin.readline

A, B = map(int, input().split())
dp = [0]

def getLog(x):
    nb, k = x , 0
    while nb > 1:
        nb //= 2
        k += 1
    return k

    
for i in range(1, getLog(B + 1) + 1):
    dp.append(dp[-1] * 2 + 2 ** (i - 1))

def getVal(x):
    if x == 0: return 0
    if x == 1: return 1
    ans = 0
    k = getLog(x+1)
    ans += dp[k]
    diff = x - 2 ** k + 1
    if diff:
        ans += diff + getVal(diff - 1)
    return ans

print(getVal(B) - getVal(A-1))