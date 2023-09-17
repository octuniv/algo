import sys
input = sys.stdin.readline

ans = []
while True:
    st = input().rstrip()
    if st == 'end':
        break
    X, O = st.count('X'), st.count('O')
    empty = 9 - X - O
    if X < O or O < X-1:
        ans.append('invalid')
        continue
    last = 'X' if X > O else 'O'
    ttt = [[st[i * 3 + j] for j in range(3)] for i in range(3)]
    X, O = [0 for _ in range(3)], [0 for _ in range(3)]
    for i in range(3):
        if ttt[i][0] == ttt[i][1] == ttt[i][2]:
            if ttt[i][0] == 'X':
                X[0] += 1
            elif ttt[i][0] == 'O':
                O[0] += 1
        if ttt[0][i] == ttt[1][i] == ttt[2][i]:
            if ttt[2][i] == 'X':
                X[1] += 1
            elif ttt[2][i] == 'O':
                O[1] += 1
    if ttt[0][0] == ttt[1][1] == ttt[2][2]:
        if ttt[2][2] == 'X':
            X[2] += 1
        elif ttt[2][2] == 'O':
            O[2] += 1
    if ttt[2][0] == ttt[1][1] == ttt[0][2]:
        if ttt[2][0] == 'X':
            X[2] += 1 
        elif ttt[2][0] == 'O':
            O[2] += 1
    if (sum(X) and not sum(O) and last == 'X') or (sum(O) and not sum(X) and last =='O') or (not (sum(X) or sum(O)) and not empty):
        ans.append('valid')
    else:
        ans.append('invalid')
print(*ans, sep='\n')