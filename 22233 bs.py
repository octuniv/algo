import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = []
for _ in range(N):
    words.append(input().strip())
    
words.sort()
vis = [1 for _ in range(N)]
ans = []

for _ in range(M):
    write = input().rstrip().split(',')
    for w in write:
        min_x = 0
        max_x = N-1
        while min_x < max_x:
            h = (min_x + max_x) // 2
            if words[h] == w:
                vis[h] = 0
                min_x = max_x = h
            elif words[h] < w:
                min_x = h + 1
            else:
                max_x = h
    ans.append(sum(vis))

for a in ans:
    print(a)

