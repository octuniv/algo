import sys
input = sys.stdin.readline

arr = []
N = int(input())
a, b, c = map(int, input().split())
arr.append([a, b, c])
for i in range(1, N):
    a, b, c = map(int, input().split())
    arr.append([a + min(arr[i-1][1], arr[i-1][2]), b + min(arr[i-1][0], arr[i-1][2]), c + min(arr[i-1][0], arr[i-1][1])])
print(min(arr[-1]))