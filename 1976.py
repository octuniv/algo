import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

joint = [i for i in range(N+1)]
height = [1 for _ in range(N+1)]

def find(x):
    if x == joint[x]: return x
    joint[x] = find(joint[x])
    return joint[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if height[x] < height[y]: joint[x] = y
        elif height[y] < height[x]: joint[y] = x
        else:
            joint[x] = y
            height[x] += 1
        
for i in range(N):
    p = list(map(int, input().split()))
    for j in range(N):
        if p[j]:
            union(i + 1, j + 1)
            
route = list(map(int, input().split()))

ans = True
start = route[0]
for p in route[1:]:
    if find(start) == find(p):
        p = start
    else:
        ans = False
        break
print('YES' if ans else 'NO')