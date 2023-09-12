import sys
input = sys.stdin.readline

src = input().rstrip()
tag = input().rstrip()

def make_res(t, c_a, c_b):
    res = False
    if len(t) == len(src) and t == src : return True
    
    if c_a > 0 and t[-1] == 'A':
        res = make_res(t[:-1], c_a - 1, c_b)
    if not res and c_b > 0 and t[0] == 'B':
        res = make_res(t[:0:-1], c_a, c_b -1)
    return res

if make_res(tag, tag.count('A') - src.count('A'), tag.count('B') - src.count('B')):
    print(1)
else:
    print(0)