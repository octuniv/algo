import sys
input = sys.stdin.readline
    
N = int(input())
graph = dict()
for _ in range(N-1):
    s, e = map(int, input().split())
    if s not in graph: graph[s] = set()
    if e not in graph: graph[e] = set()
    graph[s].add(e)
    graph[e].add(s)
dp = [0 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
ans = 0
def crd(x):
    return x * (x-1) // 2

st = []
visited[1] = 1
st.append(1)
while st:
    cur = st.pop()
    iterg = {*graph[cur]}
    for e in iterg:
        if visited[e]:
            graph[cur].remove(e)
        else:
            st.append(e)
            visited[e] = 1
    
for k in graph.keys():
    graph[k] = list(graph[k])

st, res = [1], []
while st:
    ind = st.pop()
    res.append(ind)
    for n_ind in graph[ind]:
        st.append(n_ind)
        
for ind in res[::-1]:
    dp[ind] = 1
    for c in graph[ind]:
        dp[ind] += dp[c]
    ans += crd(N) - crd(N - dp[ind])
print(ans - crd(N))