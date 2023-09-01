import sys
input = sys.stdin.readline

N, D = map(int, input().split())
path = []
for _ in range(N):
    path.append([*map(int, input().split())])

path.sort(key=lambda x: (x[1], x[2]))

shorts = [i for i in range(10001)]
renew = []
for st, ed, dist in path:
    for i in renew:
        if i > st : break
        shorts[st] = min(shorts[st], st - i + shorts[i])
    shorts[ed] = min(shorts[ed], shorts[st] + min(dist, ed - st))
    renew.append(ed)
    
print(min(shorts[i] + D - i for i in range(D+1)))