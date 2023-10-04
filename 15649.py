import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0 for _ in range(N+1)]
st = [1]
visited[1] = 1
b_c = False

while st:
    if len(st) == M: 
        if st[0] != 0:
            print(*st, sep=' ')
        r = st[-1] + 1
        while r <= N:
            if not visited[r]:
                visited[r] = 1
                visited[st[-1]] = 0
                st[-1] = r
                break
            r += 1
        if r > N: 
            visited[st[-1]] = 0
            b_c = True
            st.pop()
    else:
        if b_c:
            r = st[-1] + 1
            while r <= N:
                if not visited[r]:
                    visited[r] = 1
                    visited[st[-1]] = 0
                    st[-1] = r
                    break
                r += 1
            if r > N:
                visited[st[-1]] = 0
                st.pop()
                continue 
            b_c = False
        nr = 1
        while nr <= N:
            if not visited[nr]:
                visited[nr] = 1
                st.append(nr)
                break
            nr += 1