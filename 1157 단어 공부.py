import sys
input = sys.stdin.readline

word = input().strip()
A = ord("A")
Z = ord("Z")
a = ord("a")
alp = [0] * (Z - A + 1)
for w in word:
    seq = ord(w)
    if seq >= a:
        alp[seq - a] += 1
    else:
        alp[seq - A] += 1
mW = 0
ans_seq = 0
cnt = 0
for c in range(len(alp)):
    if mW < alp[c]:
        mW = alp[c]
        ans_seq = c
        cnt = 1
    elif mW == alp[c]:
        cnt += 1
if cnt > 1:
    print("?")
else:
    print(chr(ans_seq + A))