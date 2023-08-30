import sys
input = sys.stdin.readline

T = int(input())
ans_list = list()
for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    max_seq = sorted([i for i in range(N)], key=lambda x: -stocks[x])
    
    idx = 0
    ans = 0
    for m_v in max_seq:
        if idx >= m_v : continue
        max_val = stocks[m_v]
        for i in range(idx, m_v):
            ans += max(0, max_val - stocks[i])
        idx = m_v
    ans_list.append(ans)
    
for ans in ans_list:
    print(ans)