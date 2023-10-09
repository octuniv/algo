import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
    
ans = 0

def f(c, x):
    global ans
    
    if c == N:
        if x == M:
            ans += 1
        return
    f(c+1, x)
    f(c+1, x + arr[c])

f(0, 0)
if M == 0:
    ans -= 1
print(ans)