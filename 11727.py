import sys
input = sys.stdin.readline

d = [0, 1, 3]
for i in range(3, 1001):
    d.append((d[i-1] + 2 * d[i-2]) % 10007)

N = int(input())
print(d[N])