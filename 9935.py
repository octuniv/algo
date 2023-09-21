import sys
input = sys.stdin.readline

strings = list(input().rstrip())
boom = list(input().rstrip())
st = []
cnt, end = 0, len(strings)
while cnt < end:
    st.append(cnt)
    if len(st) >= len(boom):
        exist = True
        for i in range(len(boom)):
            if boom[-(i+1)] != strings[st[-(i+1)]]:
                exist = False
                break
        if exist:
            for _ in range(len(boom)):
                st.pop()
    cnt += 1
    
ans = ''.join([strings[i] for i in st])
print(ans if ans else 'FRULA')