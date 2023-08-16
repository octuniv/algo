import sys
input = sys.stdin.readline

N, X = map(int, input().split())
vt = list(map(int, input().split()))

ans = sub_arr = sum(vt[:X])
du = 1

for i in range(X, N):
    sub_arr += vt[i]
    sub_arr -= vt[i - X]
    if ans < sub_arr:
        ans = sub_arr
        du = 1
    elif ans == sub_arr:
        du += 1
if ans > 0:
    print(ans)
    print(du)
else:
    print("SAD")