import sys
input = sys.stdin.readline

N, M = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()
ste = house[-1] - house[0]

def sol_dis(d):
    st = 0
    cnt = 1
    for i in range(N-1):
        diff = house[i+1] - house[st]
        if diff >= d:
            st = i + 1
            cnt += 1
    return cnt

s, e = 1, ste
ans = 0
while s <= e:
    h = (s + e) // 2
    c = sol_dis(h)
    if c < M:
        e = h - 1
    elif c >= M:
        ans = h
        s = h + 1
print(ans)