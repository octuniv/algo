import sys
input = sys.stdin.readline

N = int(input())
bs = []
for _ in range(N):
    bs.append([*map(int, input().split())])

st = []
ans = 0
for _, y in bs:
    if not st or st[-1] < y:
        st.append(y)
    else:
        while True:
            if not st or st[-1] <= y:
                break
            ans += 1
            l = st.pop()
        if not st or st[-1] < y:
            st.append(y)
            
while st:
    l = st.pop()
    if l != 0:
        ans += 1
print(ans)
