import sys
input = sys.stdin.readline

N, M = map(int, input().split())
el = list(map(int, input().split()))

plug_in = set()
ans = 0
for i in range(M):
    if el[i] not in plug_in:
        if len(plug_in) >= N:
            t = set(plug_in)
            for j in range(i+1, M):
                if len(t) == 1:
                    break
                if el[j] in t:
                    t.remove(el[j])
            plug_in.remove(t.pop())
            ans += 1
        plug_in.add(el[i])
print(ans)