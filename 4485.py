import sys
input = sys.stdin.readline
from collections import deque

dirt = ((0, 1), (0, -1), (1, 0), (-1, 0))
ans = []
while True:
    N = int(input())
    if N == 0: break
    arr = []
    for _ in range(N):
        arr.append([*map(int, input().split())])
    visited = [[156251 for _ in range(N)] for _ in range(N)]
    q = deque()
    visited[0][0] = arr[0][0]
    q.append([0,0])
    
    while q:
        px, py = q.popleft()
        pv = visited[px][py]
        for i in range(4):
            dx, dy = px + dirt[i][0], py + dirt[i][1]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            dv = pv + arr[dx][dy]
            if dv < visited[dx][dy]:
                visited[dx][dy] = dv
                q.append([dx, dy])
    ans.append(visited[N-1][N-1])

for i in range(len(ans)):
    print(f'Problem {i+1}: {ans[i]}')