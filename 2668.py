import sys
input = sys.stdin.readline
import itertools

N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
coord = set(arr)
coord.remove(0)
check = [False for _ in range(N+1)]
ans_list = []
for c in coord:
    if check[c]:
        continue
    check[c] = True
    visited = [False for _ in range(N+1)]
    st = arr[c]
    visited[st] = True
    while True:
        nst = arr[st]
        if nst == c:
            visited[c] = True
            break
        elif visited[nst]:
            break
        visited[nst] = True
        st = nst
    if visited[c]:
        ans = []
        for idx in range(N+1):
            if visited[idx]:
                ans.append(idx)
                check[idx] = True
        ans_list.append(ans)
ans_list = sorted([*itertools.chain(*ans_list)])
print(len(ans_list))
print(*ans_list, sep='\n')