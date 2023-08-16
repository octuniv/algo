import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
h = deque([i for i in range(1, N + 1)])
while len(h) > 1:
    h.popleft()
    c = h.popleft()
    h.append(c)
print(h[0])