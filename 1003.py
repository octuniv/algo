import sys
input = sys.stdin.readline

fi = [[1, 0], [0, 1]]
for i in range(2, 41):
    fi.append([fi[i-1][0] + fi[i-2][0], fi[i-1][1] + fi[i-2][1]])
N = int(input())
for _ in range(N):
    print(*fi[int(input())], sep=' ')