import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().rstrip()
    K = int(input())
    alpha = [[] for _ in range(26)]
    for idx in range(len(W)):
        alpha[ord(W[idx]) - ord('a')].append(idx)
    min_ans = 10001
    max_ans = -1
    for ap in alpha:
        for a in range(len(ap) - K + 1):
            val = ap[a + K - 1] - ap[a]
            min_ans = min(min_ans, val)
            max_ans = max(max_ans, val)
    if max_ans == -1:
        print(-1)
    else:
        print(f"{min_ans+1} {max_ans+1}")