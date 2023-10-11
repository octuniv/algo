from pprint import pprint
import sys
input = sys.stdin.readline

steakers = []
N, M, K = map(int, input().split())
space = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    R, C = map(int, input().split())
    s = []
    for _ in range(R):
        s.append([*map(int, input().split())])
    steakers.append(s)

def rotate(st):
    return [list(r)[::-1] for r in zip(*st)]

def can_fill(st):
    size = [len(st), len(st[0])]
    
    for i in range(N):
        if size[0] > N - i: break
        for j in range(M):
            if size[1] > M - j: break
            check = True
            for k in range(size[0]):
                for l in range(size[1]):
                    if st[k][l] and space[i+k][j+l]:
                        check = False
                        break
                if not check: break
            if check:
                for k in range(size[0]):
                    for l in range(size[1]):
                        if st[k][l]:
                            space[i+k][j+l] = 1
                return True
    return False

ans = 0
for st in steakers:
    if not can_fill(st): 
        for _ in range(3):
            st = rotate(st)
            if can_fill(st):
                break

for i in range(N):
    for j in range(M):
        if space[i][j]:
            ans += 1
print(ans)