import sys
input = sys.stdin.readline

a = ord('A')
alp_map = {chr(a + i) : i for i in range(26)}
dirc = ((0, 1), (0, -1), (1, 0), (-1, 0))

R, C = map(int, input().split())
inp = []
for _ in range(R):
    inp.append([*input().rstrip()])
visited = [False for _ in range(26)]
st = []
st.append([0, 0, -1])
visited[alp_map[inp[0][0]]] = True
ans = 0
while st:
    x, y, p_d = st[-1]
    ans = max(ans, len(st))
    for i in range(p_d + 1, 4):
        nx, ny = x + dirc[i][0], y + dirc[i][1]
        if 0 <= nx < R and 0 <= ny < C and not visited[alp_map[inp[nx][ny]]]:
            st[-1][2] = i
            visited[alp_map[inp[nx][ny]]] = True
            st.append([nx, ny, -1])
            break
    if x == st[-1][0] and y == st[-1][1]:
        visited[alp_map[inp[x][y]]] = False
        st.pop()
print(ans)