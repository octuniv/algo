import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    p, c = map(int, input().split())
    graph[c].append(p)
    graph[p].append(c)

def DFS(x, cnt):
    ans = -1
    if x == B:
        ans = cnt
    else:
        for dest in graph[x]:
            if not visited[dest]:
                visited[dest] = 1
                ans = max(ans,DFS(dest, cnt + 1))
    return ans

visited[A] = 1
print(DFS(A, 0))