import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    s, e = map(int, input().split())
    graph[s].append([e, i])
    graph[e].append([s, i])

visited = [N * M for _ in range(N+1)]
visited[1] = 0
hp = [[0, 1]]

while hp:
    past_cost, s = heapq.heappop(hp)
    
    if visited[s] < past_cost: continue
    
    for e, n_t in graph[s]:
        nc = past_cost + (n_t - past_cost) % M
        if nc + 1 < visited[e]:
            visited[e] = nc + 1
            heapq.heappush(hp, [nc + 1, e])
print(visited[N])