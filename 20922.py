import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [*map(int, input().split())]
exist = [0 for _ in range(100001)]
ans = 0
st = 0
ed = 0

while ed < N:
    if exist[arr[ed]] < K:
        exist[arr[ed]] += 1
        ed += 1
    else:
        exist[arr[st]] -= 1
        st += 1
        
    ans = max(ans, ed - st)
        

print(ans)