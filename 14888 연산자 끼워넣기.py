import sys
input = sys.stdin.readline

min_val = pow(10, 10) + 1
max_val = -pow(10, 10) - 1

nums = []
ops = []
visited = []
op_def = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: int(x / y)
]

def perm(sums, k):
    global min_val, max_val
    if N - 1 == k:
        min_val = min(sums, min_val)
        max_val = max(sums, max_val)
        return
    
    for i in range(N - 1):
        if not visited[i]:
            visited[i] = True
            new_sums = op_def[ops[i]](sums, nums[k + 1])
            perm(new_sums, k + 1)
            visited[i] = False
            
N = int(input())
nums = list(map(int, input().split()))
op_in = list(map(int, input().split()))
for i in range(4):
    for j in range(op_in[i]):
        ops.append(i)
visited = [False] * (N - 1)
perm(nums[0], 0)
print(max_val)
print(min_val)