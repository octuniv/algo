import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ns = [[]] * (N + 1)
while N:
    inp = list(map(int, input().split()))
    ns[inp[0]] = inp[1:]
    N -= 1
find_it = ns[K]
ns.sort(reverse=True)
ns.insert(0, [])
prev = [-1, -1, -1]
ans = 1
for i in range(1, len(ns)):
    if not all(x == y for x, y in zip(ns[i], prev)):
        prev = ns[i]
        ans = i
        
    if all(x == y for x, y in zip(ns[i], find_it)):
        print(ans)
        break
    
