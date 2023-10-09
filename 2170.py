import sys
input = sys.stdin.readline

N = int(input())
line = []
for _ in range(N):
    a, b = map(int, input().split())
    line.append([a, b])

line.sort()
mn_v, mx_v = line[0]
ans = 0
for i in range(1,N):
    a, b = line[i]
    if mx_v < a:
        ans += mx_v - mn_v
        mn_v = a
    mx_v = max(mx_v, b)

ans += mx_v - mn_v
print(ans)