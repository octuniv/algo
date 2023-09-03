import sys
input = sys.stdin.readline

N = int(input())
balls = [*input().rstrip()]

r_elems = []
b_elems = []
b_color, c_start = balls[0], 0

for idx in range(1, N):
    if b_color != balls[idx]:
        if b_color == "R":
            r_elems.append([c_start, idx])
        else:
            b_elems.append([c_start, idx])
        c_start = idx
        b_color = balls[idx]

if b_color == "R":
    r_elems.append([c_start, N])
else:
    b_elems.append([c_start, N])

if not (r_elems and b_elems):
    print(0)
else:
    ans = N
    tp = 0 if r_elems[0][0] == 0 else r_elems[0][1] - r_elems[0][0]
    for idx in range(1, len(r_elems)):
        tp += r_elems[idx][1] - r_elems[idx][0]
    ans = min(ans, tp)
    tp = 0 if r_elems[-1][1] == N else r_elems[-1][1] - r_elems[-1][0]
    for idx in range(len(r_elems) - 1):
        tp += r_elems[idx][1] - r_elems[idx][0]
    ans = min(ans, tp)
    tp = 0 if b_elems[0][0] == 0 else b_elems[0][1] - b_elems[0][0]
    for idx in range(1, len(b_elems)):
        tp += b_elems[idx][1] - b_elems[idx][0]
    ans = min(ans, tp)
    tp = 0 if b_elems[-1][1] == N else b_elems[-1][1] - b_elems[-1][0]
    for idx in range(len(b_elems) - 1):
        tp += b_elems[idx][1] - b_elems[idx][0]
    ans = min(ans, tp)
    print(ans)