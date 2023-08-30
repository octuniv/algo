import sys
import heapq
input = sys.stdin.readline

N = int(input())
table = list()
for _ in range(N):
    table.append([*map(int, input().split())])
hp = []

for i in range(N):
    heapq.heappush(hp, [-table[N-1][i], i, N - 1])

idx = 0
ans = -1
while idx < N:
    val, col, row = heapq.heappop(hp)
    ans = -val
    if row > 0:
        heapq.heappush(hp, [-table[row - 1][col], col, row - 1])
    idx += 1
        
print(ans)