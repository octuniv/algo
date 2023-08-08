import sys
input = sys.stdin.readline

a = list(input().strip())

left = 0
l = False
ans = 0

for b in a:
    if b == '(':
        left += 1
        l = True
    else:
        left -= 1
        if l:
            ans += left
        else:
            ans += 1
        l = False

print(ans)