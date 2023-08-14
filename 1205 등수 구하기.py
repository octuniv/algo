import sys
input = sys.stdin.readline

N, C, P = map(int, input().split())

if N != 0:
    ps = list(map(int, input().split()))
    ps = [[c, 0] for c in ps]
else:
    ps = []

ps.append([C, 1])
ps.sort(key=lambda x: (-x[0], -x[1]))
ans = -1

a = min(P, len(ps))
for i in range(a):
    if ps[i][1] == 1:
        ans = i + 1

if a < len(ps) and ps[a][0] == C:
    ans = -1
    
print(ans)