import sys
input = sys.stdin.readline

N = int(input())
towers = [*map(int, input().split())]
stack = []
ans = [0 for _ in range(N)]
for t in range(N-1, -1, -1):
    val = towers[t]
    while stack and stack[-1][0] < val:
        prev = stack.pop()
        ans[prev[1]] = t + 1
    stack.append([val, t])
print(*ans)