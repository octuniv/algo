import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = [*map(int, input().split())]
ans = N + 1
start, end, sub = 0, -1, 0
while start < N:
    if start >= end:
        end += 1
        if end >= N:
            break
        sub += arr[end]
    else:
        if sub < S:
            end += 1
            if end >= N:
                break
            sub += arr[end]
        else:
            sub -= arr[start]
            start += 1
    
    if sub >= S:
        ans = min(ans, end - start + 1)

print(ans if ans <= N else 0)