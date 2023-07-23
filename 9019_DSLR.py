from collections import deque
from copy import copy
import sys
input = sys.stdin.readline

def D(n):
    return (n * 2) % 10000

def S(n):
    return (n - 1) % 10000

def L(n):
    over = int(n / 1000)
    return (n * 10) % 10000 + over

def R(n):
    under = n % 10
    return int(n / 10) + under * 1000

func_arr = [D, S, L, R]

size = int(input())

for _ in range(size):
    visited = [False] * 10001
    q = deque()
    F, C = map(int, input().split())
    q.append([[], F])
    visited[F] = True
    while q:
        lt, pnum = q.popleft()
        if pnum == C:
            print(''.join(lt))
            break
        
        for func in func_arr:
            nnum = func(pnum)
            if not visited[nnum]:
                visited[nnum] = True
                nlt = copy(lt)
                nlt.append(func.__name__)
                q.append([nlt, nnum])