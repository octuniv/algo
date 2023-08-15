import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lamps = list(map(int, input().split()))

def lines_ok(lr):
    pv, ed = lr[0]
    if pv > 0:
        return False
    for nv in lr[1:]:
        if ed < nv[0]:
            return False
        ed = nv[1]
    if ed >= N:
        return True
    else:
        return False
        
min_l = 1
max_l = N
while min_l < max_l:
    h = (min_l + max_l) // 2
    lights = [[lp - h, lp + h] for lp in lamps]
    if lines_ok(lights):
        max_l = h
    else:
        min_l = h + 1
        
print(max_l)