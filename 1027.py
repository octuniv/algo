import sys
input = sys.stdin.readline

N = int(input())
bs = list(map(int, input().split()))
ans = 0
for i in range(N):
    tp = 0
    if i > 0:
        low, high = -sys.maxsize, -1
        for j in range(i-1, -1, -1):
            pv = (bs[j] - bs[i]) / (i - j)
            if pv < 0 and high < 0 and low < pv:
                low = pv
                tp += 1
            elif pv >= 0 and pv > high:
                high = pv
                tp += 1
    if i < N - 1:
        low, high = -sys.maxsize, -1
        for j in range(i+1, N):
            pv = (bs[j] - bs[i]) / (j - i)
            if pv < 0 and high < 0 and low < pv:
                low = pv
                tp += 1
            elif pv >= 0 and pv > high:
                high = pv
                tp += 1
    ans = max(ans, tp)
print(ans)