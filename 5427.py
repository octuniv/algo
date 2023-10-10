import sys
from collections import deque
input = sys.stdin.readline

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def set_bound(w, h):
    return lambda x, y: x < 0 or y < 0 or x >= w or y >= h
disable_block = ['#', '*']
T = int(input())
while T:
    T -= 1
    
    w, h = map(int, input().split())
    building = []
    fire, human = [], []
    for i in range(h):
        ln = [*input().rstrip()]
        for ww in range(len(ln)):
            if ln[ww] == '*':
                fire.append([ww, i, 'f'])
            elif ln[ww] == '@':
                human = [ww, i, 0]
        building.append(ln)
    
    over_bound = set_bound(w, h)
    q = deque(fire)
    q.append(human)
    ans = 'IMPOSSIBLE'
    while q:
        x, y, tp = q.popleft()

        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if over_bound(nx, ny):
                if tp == 'f': continue
                else: 
                    ans = tp + 1
                    break
            if building[ny][nx] not in disable_block: 
                if tp != 'f' and building[ny][nx] == '@': continue
                building[ny][nx] = '*' if tp == 'f' else '@'
                q.append([nx, ny, tp if tp == 'f' else tp + 1])
            
        if ans != 'IMPOSSIBLE':
            break
    print(ans)