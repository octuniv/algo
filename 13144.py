import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
vis = [False for _ in range(100001)]
ans, e = 0, 0
for i in range(N):
    while e < N:
        if vis[arr[e]]: break
        vis[arr[e]] = True
        e += 1
    ans += (e - i)
    vis[arr[i]] = False
    
print(ans)