import sys
input = sys.stdin.readline

e = int(input())
shooter = []
for _ in range(e):
    shooter.append(list(map(int, input().split())))
    
ans = -1
seq = [-1 for _ in range(9)]
seq[3] = 0
visited = [0 for _ in range(9)]
visited[0] = 1

def make_ans():
    global ans
    t_ans = 0
    t = 0
    hitter = 0
    while t < e:
        lane, out = [], 0
        while True:
            if out >= 3 : break
            p = shooter[t][seq[hitter]]
            if p == 0: 
                out += 1
            elif p == 4:
                t_ans += len(lane) + 1
                lane = []
            else:
                t_lane = []
                for l in lane:
                    if l + p >= 4: t_ans += 1
                    else: t_lane.append(l+p)
                t_lane.append(p)
                lane = t_lane
            hitter = (hitter + 1) % 9
        t += 1
    ans = max(ans, t_ans)
    return

def DFS(cnt):
    if cnt >= 9:
        make_ans()
        return
    if cnt == 3: cnt = 4
    for i in range(9):
        if not visited[i]:
            visited[i] = True
            seq[cnt] = i
            DFS(cnt + 1)
            visited[i] = False
    return

DFS(0)
print(ans)