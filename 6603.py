import sys
input = sys.stdin.readline

visited = []

def comb(ln, st, end):
    if len(ln) >= 6:
        print(*[inp[l + 1] for l in ln], sep=' ')
        return
    
    for i in range(st, end):
        if visited[i] : continue
        visited[i] = True
        ln.append(i)
        comb(ln, i + 1, end)
        ln.pop()
        visited[i] = False
    
nf = False
while True:
    inp = [*map(int, input().split())]
    if inp[0] == 0:
        break
    else:
        if nf:
            print()
        else:
            nf = True
    visited = [0 for _ in range(inp[0])]
    for i in range(inp[0] - 5):
        visited[i] = True
        ln = [i]
        comb(ln, i + 1, inp[0])