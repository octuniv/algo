import sys
input = sys.stdin.readline

C = int(input())
result = []
while C:
    C -= 1
    n, k, t, m = map(int, input().split())
    points = [[0 for _ in range(k)] for _ in range(n)]
    submit = [0 for _ in range(n)]
    seq = [0 for _ in range(n)]
    for cc in range(m):
        i, j, s= map(int, input().split())
        i, j = i-1, j-1
        points[i][j] = max(points[i][j], s)
        submit[i] += 1
        seq[i] = cc
    sum_p = [sum(points[i]) for i in range(n)]
    ranks = [i for i in range(n)]
    ranks.sort(key=lambda x: (-sum_p[x], submit[x], seq[x]))
    for i in range(n):
        if ranks[i] == t-1:
            result.append(i+1)
            break
for r in result:
    print(r)