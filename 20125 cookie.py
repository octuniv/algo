import sys
input = sys.stdin.readline

N = int(input())
field = [['_'] * (N + 2)]
i = 1
h_pos = [-1, -1]
while i <= N:
    in_row = ['_'] + list(input().strip()) + ['_']
    ct = 0
    for c in in_row:
        if c == '*':
            ct += 1
    if ct > 2:
        h_pos[0] = i
        for ci in range(len(field[i-1])):
            if field[i-1][ci] == '*':
                h_pos[1] = ci
                break
    field.append(in_row)
    i += 1
    
field.append(['_'] * (N + 2))
ans = [0] * 5

for i in range(h_pos[1] - 1, 0, -1):
    if field[h_pos[0]][i] == '*':
        ans[0] += 1
    else:
        break
    
for i in range(h_pos[1] + 1, N + 2):
    if field[h_pos[0]][i] == '*':
        ans[1] += 1
    else:
        break
    
heap_y = -1
for i in range(h_pos[0] + 1, N + 2):
    if field[i][h_pos[1]] == '*':
        ans[2] += 1
        heap_y = i
    else:
        break

for i in range(heap_y + 1, N + 2):
    if field[i][h_pos[1] - 1] == '*':
        ans[3] += 1
    else:
        break
    
for i in range(heap_y + 1, N + 2):
    if field[i][h_pos[1] + 1] == '*':
        ans[4] += 1
    else:
        break
    
print(f"{h_pos[0]} {h_pos[1]}")
print(f"{ans[0]} {ans[1]} {ans[2]} {ans[3]} {ans[4]}")