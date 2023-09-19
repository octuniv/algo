import sys
input = sys.stdin.readline

op = [' ', '+', '-']
t_ans = []

def ans_check(oper, opt, n):
    n_oper, n_opt = [oper[0]], []
    for i in range(n):
        if opt[i] != 0:
            n_oper.append(oper[i+1])
            n_opt.append(opt[i])
        else:
            s = n_oper.pop()
            n_oper.append(s * 10 + oper[i+1])
    c = n_oper[0]
    for i in range(len(n_opt)):
        if n_opt[i] == 1:
            c += n_oper[i+1]
        else:
            c -= n_oper[i+1]
    if c == 0:
        a = ''
        for i in range(n):
            a += str(oper[i])
            a += op[opt[i]]
        a += str(oper[-1])
        t_ans.append(a)
    return

T = int(input())
for i in range(T):
    N = int(input())
    numbers = [i for i in range(1, N + 1)]
    stack, cnt = [], 0
    if i != 0:
        t_ans.append('')
    end = False
    while not end:
        if cnt < N - 1:
            stack.append(0)
            cnt += 1
        else:
            while True:
                if not stack:
                    end = True
                    break
                if cnt == N - 1:
                    ans_check(numbers, stack, N - 1)
                if stack[-1] != 2:
                    stack[-1] += 1
                    break
                else:
                    stack.pop()
                    cnt -= 1

print(*t_ans, sep='\n')