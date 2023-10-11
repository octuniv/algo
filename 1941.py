import sys
from pprint import pprint
from itertools import combinations
from collections import deque
input = sys.stdin.readline

clr = []
d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
out_bound = lambda x, y : x < 0 or y < 0 or x >= 5 or y >= 5
for _ in range(5):
    clr.append([*input().rstrip()])
    
ans = 0

def joint(check_list):
    q = deque()
    q.append(check_list.pop())
    while q:
        p = q.popleft()
        x, y = p // 5, p % 5
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if out_bound(nx, ny): continue
            val = nx * 5 + ny
            if val in check_list:
                check_list.remove(val)
                q.append(val)
                
    if check_list: return False
    return True

def check_pr(check_list):
    p = [[v // 5, v % 5] for v in check_list]
    s = 0
    for x, y in p:
        if clr[x][y] == 'S':
            s += 1
    return s >= 4

for comb in combinations([i for i in range(25)], 7):
    comb = set(comb)
    if check_pr(comb) and joint(comb):
        ans += 1

print(ans)
