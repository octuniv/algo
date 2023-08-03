import sys
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

ans = (1 + int((H-1) / (N+1))) * (1 + int((W-1) / (M+1)))
print(ans)