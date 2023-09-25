import sys
input = sys.stdin.readline

N = int(input())
ch = []
for _ in range(N):
    ch.append(int(input()))

long = []
long.append(ch[0])
for i in range(1, N):
    t = ch[i]
    if long[-1] < ch[i]:
        long.append(t)
    else:
        st, ed = 0, len(long)
        while st < ed:
            h = (st + ed) // 2
            if long[h] >= t:
                ed = h
            else:
                st = h + 1
        long[ed] = t
print(N - len(long))
print(long)