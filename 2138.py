import sys
input = sys.stdin.readline

N = int(input())
p = [*map(int, input().rstrip())]
d = [*map(int, input().rstrip())]
ans = -1
do = []

def sOn(idx):
    for i in range(idx-1, idx+2):
        if i >= N: break
        do[i] = 0 if do[i] else 1
        
def solve(n):
    global do
    do = [*p]
    if n == 1:
        do[0] = 0 if do[0] else 1
        do[1] = 0 if do[1] else 1
        ts = 1
    else:
        ts = 0
    
    for i in range(1, N):
        if do[i-1] != d[i-1]:
            sOn(i)
            ts += 1
    
    return ts if d == do else -1


ans = solve(0)
if ans == -1:
    ans = solve(1)
print(ans)