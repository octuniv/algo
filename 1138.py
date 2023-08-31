import sys
input = sys.stdin.readline

N = int(input())
height_level = [0] + [*map(int, input().split())]
visited = [0 for _ in range(N + 1)]

for i in range(1, N+1):
    lev = height_level[i]
    for j in range(1, N+1):
        if visited[j] != 0:
            continue
        if lev > 0:
            lev -= 1
        else:
            visited[j] = i
            break

for i in visited[1:]:
    print(i, end=' ')