import sys
input = sys.stdin.readline

sent = input().rstrip()
isM = False
ans, temp = 0, 0
min_v, max_v = ord("0"), ord("9")
for i in sent:
    if i == "-":
        if isM:
            ans -= temp
        else:
            ans += temp
        isM = True
        temp = 0
    elif i == "+":
        if isM:
            ans -= temp
        else:
            ans += temp
        temp = 0
    else:
        temp = temp * 10 + int(i)

if isM:
    ans -= temp
else:
    ans += temp
print(ans)