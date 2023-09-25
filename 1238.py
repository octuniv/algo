import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
route = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, v = map(int, input().split())
    route[s].append([e, v])

hq = []
shortest_from_X = [sys.maxsize for _ in range(N+1)]
shortest_from_X[X] = 0
for to, v in route[X]:
    heapq.heappush(hq, [v, to])
    shortest_from_X[to] = v

while hq:
    v, to = heapq.heappop(hq)
    if shortest_from_X[to] < v: continue
    for nt, nv in route[to]:
        nnv = nv + v
        if shortest_from_X[nt] > nnv:
            shortest_from_X[nt] = nnv
            heapq.heappush(hq, [nnv, nt])

ans = 0
for i in range(1, N+1):
    if i == X: continue
    st = [sys.maxsize for _ in range(N+1)]
    st[i] = 0
    for to, v in route[i]:
        heapq.heappush(hq, [v, to])
        st[to] = v
    while hq:
        v, to = heapq.heappop(hq)
        if st[to] < v: continue
        if to == X: break
        for nt, nv in route[to]:
            nnv = nv + v
            if st[nt] > nnv:
                st[nt] = nnv
                heapq.heappush(hq, [nnv, nt])
    while hq:
        hq.pop()
    ans = max(ans, st[X] + shortest_from_X[i])
print(ans)