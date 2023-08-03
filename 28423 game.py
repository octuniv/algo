from functools import reduce
import sys
import math

input = sys.stdin.readline
L, R = map(int, input().split())
sol = 0

def digit_length(n):
    return int(math.log10(n)) + 1 if n else 0

def get_nums(x):
    ret = []
    while x > 0 :
        ret.append(int(x % 10))
        x = int(x / 10)
    return ret

def func(x):
    nums = get_nums(x)
    A = reduce(lambda acc, cur : acc + cur, nums, 0)
    B = reduce(lambda acc, cur : acc * cur, nums, 1)
    if B != 0:
        return A * pow(10, digit_length(B)) + B
    else:
        return A * 10
    
for n in range(L, R+1):
    stack = set()
    stack.add(n)
    nn = n
    fn = -1
    while True:
        fn = func(nn)
        if fn in stack or fn > 100000:
            break
        stack.add(fn)
        nn = fn
    if fn > 100000:
        sol += -1
    elif fn == nn:
        sol += 1
        
print(sol)
    