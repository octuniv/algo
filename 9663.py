import sys
input = sys.stdin.readline

N = int(input())
table = [0 for _ in range(15)]
ans = 0

def nq(cn):
    global ans
    if cn == N:
        ans += 1
        return
    
    for i in range(N):
        table[cn] = i
        if (possible(cn)): nq(cn + 1)
        
def possible(cn):
    for i in range(cn):
        if table[cn] == table[i] or cn - i == abs(table[cn] - table[i]):
            return False
    return True

nq(0)
print(ans)