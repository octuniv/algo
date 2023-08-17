import sys
input = sys.stdin.readline

N, K = map(int,input().split())
a = input().rstrip()
bg = []
hm = []
idx = 0
while idx < len(a):
    if a[idx] == 'H':
        bg.append(idx)
    else:
        hm.append(idx)
    idx += 1
b_idx = 0
h_idx = 0
ans = 0
if len(bg) != 0 and len(hm) != 0:
    while h_idx < len(hm):
        while b_idx < len(bg):
            if bg[b_idx] > hm[h_idx] + K : break
            elif bg[b_idx] < hm[h_idx] - K: b_idx += 1
            else:
                ans += 1
                b_idx += 1
                break
        h_idx += 1
print(ans)