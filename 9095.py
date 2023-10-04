import sys
input = sys.stdin.readline

arr = [0,1,2,4]
for i in range(4, 12):
    arr.append(arr[i-3] + arr[i-2] + arr[i-1])
out = []

N = int(input())
for _ in range(N):
    C = int(input())
    out.append(arr[C])
print(*out, sep='\n')