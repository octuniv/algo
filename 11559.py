from pprint import pprint
import sys
from collections import deque
input = sys.stdin.readline

puyo = []

for _ in range(12):
    puyo.append([*input().rstrip()])

def find_combo():
    visited = [[0 for _ in range(6)] for _ in range(12)]
    d = [[-1, 0], [0, 1], [0, -1]]
    combo = []
    over_bound = lambda x, y: x < 0 or y < 0 or y >= 6 or x >= 12
    for i in range(11, -1, -1):
        for j in range(6):
            if not visited[i][j] and puyo[i][j] != '.':
                puyo_type = puyo[i][j]
                visited[i][j] = 1
                temp = [[i, j]]
                q = deque()
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    for z in range(3):
                        nx, ny = x + d[z][0], y + d[z][1]
                        if over_bound(nx, ny): continue
                        if visited[nx][ny]: continue
                        if puyo[nx][ny] == puyo_type:
                            visited[nx][ny] = 1
                            temp.append([nx, ny])
                            q.append([nx, ny])
                if len(temp) >= 4:
                    combo.extend(temp)
    return combo

def delete_puyo(combo):
    deleted_for_cols = [set() for _ in range(6)]
    for d in combo:
        deleted_for_cols[d[1]].add(d[0])
    for i in range(6):
        if deleted_for_cols[i]:
            p_cnt = 11
            for j in range(11, -1, -1):
                if j not in deleted_for_cols[i]:
                    puyo[p_cnt][i] = puyo[j][i]
                    p_cnt -= 1
            while p_cnt > 0:
                puyo[p_cnt][i] = '.'
                p_cnt -= 1
    return

ans = 0

while True:
    combo = find_combo()
    if not combo:
        break
    delete_puyo(combo)
    ans += 1
print(ans)