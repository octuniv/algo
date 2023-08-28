import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name = dict()
for _ in range(N):
    t, p = input().split()
    if not int(p) in name:
        name[int(p)] = t
levels = sorted([p for p in name.keys()])
level_end = len(levels) - 1
answer = []
for _ in range(M):
    point = int(input())
    mn_l = 0
    mx_l = level_end
    while mn_l < mx_l:
        h = (mn_l + mx_l) // 2
        if levels[h] == point:
            mn_l = mx_l = h
        if levels[h] < point:
            mn_l = h+1
        else:
            mx_l = h
    answer.append(name[levels[mx_l]])
for a in answer:
    print(a)