import sys
input = sys.stdin.readline

T = int(input())
input_list = []
max_in = 0
for _ in range(T):
    N = int(input())
    input_list.append(N)
    max_in = max(max_in, N)
    
dp = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1]]
idx = 4
while idx <= max_in:
    dp.append([])
    dp[-1].append(1)
    dp[-1].append(sum(dp[-3][:2]))
    dp[-1].append(sum(dp[-4][:3]))
    idx += 1

for idx in input_list:
    print(sum(dp[idx]))