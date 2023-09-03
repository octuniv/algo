import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
cp = []
sushis = []
choices = [0 for _ in range(d+1)]
choices[c] = 1
num_choice = 1
ans = 0

for i in range(N):
    ss = int(input())
    sushis.append(ss)

sushis.extend(sushis[:k-1])

for idx in range(k-1):
    s = sushis[idx]
    if not choices[s]:
        num_choice += 1
    choices[s] += 1
    
for idx in range(k-1, N + k - 1):
    s = sushis[idx]
    if not choices[s]:
        num_choice += 1
    choices[s] += 1
    ans = max(ans, num_choice)
    d = sushis[idx-k+1]
    choices[d] -= 1
    if not choices[d]:
        num_choice -= 1

print(ans)