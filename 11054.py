import sys
input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]
dp_I = [0 for _ in range(N)]
dp_R = [0 for _ in range(N)]

for i in range(N):
    dp_I[i] = 1
    for j in range(0, i):
        if arr[j] < arr[i] and dp_I[i] < dp_I[j] + 1:
            dp_I[i] = dp_I[j] + 1

for i in range(N-1, -1, -1):
    dp_R[i] = 1
    for j in range(i + 1, N):
        if arr[j] < arr[i] and dp_R[i] < dp_R[j] + 1:
            dp_R[i] = dp_R[j] + 1

ans = 0
for i in range(N):
    f = dp_I[i]
    e = dp_R[i] - 1
    ans = max(ans, f+e)
print(ans)