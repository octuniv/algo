import sys
input = sys.stdin.readline

N = int(input())
pilars = list()
for _ in range(N):
    f, h = map(int, input().split())
    pilars.append([f, h])

pilars.sort(key=lambda x: -x[1])
f, h = pilars[0]
max_h = h
f_idx = f
e_idx = f + 1
ans = h
for p_idx in range(1, len(pilars)):
    f, h = pilars[p_idx]
    e = f + 1
    if f < f_idx:
        ans += h * (f_idx - f)
        f_idx = f
    elif e > e_idx:
        ans += h * (e - e_idx)
        e_idx = e
print(ans)