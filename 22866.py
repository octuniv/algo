import sys
input = sys.stdin.readline

N = int(input())
bs = [0, *list(map(int, input().split()))]
view = [[[], []] for _ in range(N+1)]
st = []
for i in range(1, N+1):
    while st:
        if st[-1][0] <= bs[i]:
            st.pop()
        else:
            break
    view[i][0] = [len(st), st[-1][1]] if st else [0]
    st.append([bs[i], i])
while st:
    st.pop()

for i in range(N, 0, -1):
    while st:
        if st[-1][0] <= bs[i]:
            st.pop()
        else:
            break
    view[i][1] = [len(st), st[-1][1]] if st else [0]
    st.append([bs[i], i])

for i in range(1, N+1):
    l = view[i][0][0] + view[i][1][0]
    a = 0
    if l:
        if view[i][1][0] and view[i][0][0]:
            if i - view[i][0][1] > view[i][1][1] - i:
                a = view[i][1][1]
            else:
                a = view[i][0][1]
        elif view[i][0][0]:
            a = view[i][0][1]
        else:
            a = view[i][1][1]
        print(f'{l} {a}')
    else:
        print(0)