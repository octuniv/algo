import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = set()
ans = list()
for _ in range(N):
    words.add(input().strip())

for _ in range(M):
    write = input().rstrip().split(',')
    for w in write:
        if w in words:
            words.remove(w)
    ans.append(len(words))

for a in ans:
    print(a)