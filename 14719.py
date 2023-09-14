import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block = [*map(int, input().split())]
left = right = -1
l_v = r_v = -1
ans = 0

for i in range(W):
    if l_v < block[i]:
        left = right = i
        l_v = r_v = block[i]

while left > 0:
    p_l = left
    l_v = -1
    for i in range(left):
        if l_v < block[i]:
            left = i
            l_v = block[i]
    for i in range(p_l - 1, left, -1):
        ans += l_v - block[i]
        
while right < W - 2:
    p_r = right
    r_v = -1
    for i in range(right + 1, W):
        if r_v < block[i]:
            right = i
            r_v = block[i]
    for i in range(p_r + 1, right):
        ans += r_v - block[i]

print(ans)