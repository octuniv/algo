import sys
input = sys.stdin.readline

nicks = set()
tt = {
    'Y' : 1,
    'F' : 2,
    'O' : 3
}
N, C = map(str, input().split())
N = int(N)
gm = tt[C]
c = 0
ans = 0

while N:
    N -= 1
    nick = input().strip()
    if nick not in nicks:
        nicks.add(nick)
        c += 1
        if c >= gm:
            ans += 1
            c = 0
            
print(ans)