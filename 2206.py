import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
lab = []
for _ in range(N):
    lab.append(list(map(int, input().rstrip())))

mv = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
q = deque()
q.append([0,0,0]) # x, y, wallbreak
visited[0][0][0] = 1
ans = -1

while q:
    x, y, wallb = q.popleft()
    
    if x == N-1 and y == M-1:
        ans = visited[x][y][wallb]
        break
    
    for m in range(4):
        nx, ny, nw = x + mv[m][0], y + mv[m][1], wallb
        if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny][wallb]:
            continue
        if lab[nx][ny]:
            if wallb:
                continue
            else:
                nw = 1
        visited[nx][ny][nw] = visited[x][y][wallb] + 1
        q.append([nx, ny, nw])

print(ans)