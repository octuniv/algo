import sys
input = sys.stdin.readline

st = list(map(int, input().rstrip()))
vis = [1 for _ in range(len(st))]
bn = [0, 0]
for b in st:
    bn[b] += 1
bn = [b // 2 for b in bn]
for i in range(len(st)):
    if bn[1] == 0:
        break
    if st[i] == 1:
        bn[1] -= 1
        vis[i] = 0
for i in range(len(st) -1, -1, -1):
    if bn[0] == 0:
        break
    if st[i] == 0:
        bn[0] -= 1
        vis[i] = 0
for i in range(len(st)):
    if vis[i]:
        print(st[i], end='')