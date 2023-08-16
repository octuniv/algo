import sys
input = sys.stdin.readline

N = int(input())
rs = list(map(int, input().split()))
M = int(input())

def bg_ok(bg):
    global M
    acc = 0
    for c in rs:
        acc += min(bg, c)
    return acc <= M

min_bg = 0
max_bg = max(rs)
ans = 1

while min_bg <= max_bg:
    h = (min_bg + max_bg) // 2
    if bg_ok(h):
        ans = h
        min_bg = h + 1
    else:
        max_bg = h - 1
print(ans)