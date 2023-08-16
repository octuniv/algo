import sys
input = sys.stdin.readline

N = int(input())
leng = list(map(int, input().split()))
cost = list(map(int, input().split()))
ans = 0
min_cost = 1000000001

for i in range(N - 1):
    min_cost = min(min_cost, cost[i])
    ans += min_cost * leng[i]

print(ans)