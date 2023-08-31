import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort()

visited = [0 for _ in range(N+1)]

visited[V] = 1
stack = [[V, 0]]
answer_dfs = []
while stack:
    dept, st = stack.pop()
    if st == 0:
        answer_dfs.append(dept)
    for dest_idx in range(st, len(graph[dept])):
        dest = graph[dept][dest_idx]
        if visited[dest]:
            continue
        visited[dest] = 1
        stack.append([dept, dest_idx + 1])
        stack.append([dest, 0])
        break

queue = deque()
visited = [0 for _ in range(N+1)]

visited[V] = 1
queue.append(V)
answer_bfs = []

while queue:
    dept = queue.popleft()
    answer_bfs.append(dept)
    for dest in graph[dept]:
        if visited[dest]:
            continue
        visited[dest] = 1
        queue.append(dest)

print(*answer_dfs)
print(*answer_bfs)