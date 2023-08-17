from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mape = [list(map(int, input().split())) for _ in range(N)]

m_dir = [[1, -1], [1, 0], [1, 1]]
dis = [[[10000 for _ in range(3)] for _ in range(M)] for _ in range(N)]
q = deque()
for i in range(M):
    dis[0][i] = [mape[0][i] for _ in range(3)]
    q.append([[0, i], mape[0][i], -1])
    
while q:
    [x_pos, y_pos], p_val, p_dir = q.popleft()
    if x_pos == N - 1: continue
    for dir in range(3):
        if dir == p_dir: continue
        nx, ny = x_pos + m_dir[dir][0], y_pos + m_dir[dir][1]
        if ny < 0 or ny >= M: continue
        nv = p_val + mape[nx][ny]
        if dis[nx][ny][dir] >= nv:
            dis[nx][ny][dir] = nv
            q.append([[nx, ny], nv, dir])
        
ans = 10000
for c in dis[-1]:
    for d in c:
        ans = min(ans, d)
print(ans)