import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
farmers = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    farmers[a].append([b, c])
    farmers[b].append([a, c])
    
dist = [50050000 for _ in range(N+1)]
dist[1] = 0
q = []
heapq.heappush(q, [0, 1])

while q:
    cow, dept = heapq.heappop(q)
    for [dest, d_cow] in farmers[dept]:
        n_cow = d_cow + cow
        if dist[dest] > n_cow:
            dist[dest] = n_cow
            heapq.heappush(q, [n_cow, dest])
            
print(dist[N])