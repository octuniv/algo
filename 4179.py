import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
lab = []
human = []
dt = ((0, 1), (0, -1), (1, 0), (-1, 0))
q = deque()
ans = 0
for i in range(R):
    line = list(input().rstrip())
    for j in range(C):
        if line[j] == 'J':
            human = [i,j]
        elif line[j] == 'F':
            q.append(['F',i,j,0])
    lab.append(line)
    
q.appendleft(['J', human[0], human[1], 0])

while q:
    tp, x, y, cnt = q.popleft()
    if tp == 'J' and lab[x][y] != 'J':
        continue
    for i in range(4):
        nx, ny = x + dt[i][0], y + dt[i][1]
        if 0 <= nx < R and 0 <= ny < C:
            if lab[nx][ny] == '#': continue
            if tp == 'J' and lab[nx][ny] == '.':
                lab[nx][ny] = 'J'
                q.append(['J', nx, ny, cnt + 1])
            elif tp == 'F' and lab[nx][ny] != 'F':
                lab[nx][ny] = 'F'
                q.append(['F', nx, ny, cnt + 1])
        elif tp == 'J':
            ans = cnt + 1
            break
    
    if ans: break
    
print(ans if ans else 'IMPOSSIBLE')