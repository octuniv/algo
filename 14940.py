import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [[0 for _ in range(M+2)]]
start = []
for _ in range(N):
    maps.append([0] + [*map(int, input().split())] + [0])
    if not start:
        for j in range(M+2):
            if maps[-1][j] == 2:
                start = [len(maps) - 1, j]
maps.append([0 for _ in range(M+2)])
m_dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
ans = [[0 for _ in range(M+2)] for _ in range(N+2)]
q = deque()
q.append([*start, 0])
ans[start[0]][start[1]] = -1
while q:
    r, w, d = q.popleft()
    for dr, dw in m_dirs:
        nr, nw = r + dr, w + dw
        if ans[nr][nw] or not maps[nr][nw]: continue
        ans[nr][nw] = d+1
        q.append([nr, nw, d+1])

ans[start[0]][start[1]] = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if not ans[i][j] and maps[i][j]:
            ans[i][j] = -1

ans[start[0]][start[1]] = 0
for i in range(1, N+1):
    print(*ans[i][1:M+1])