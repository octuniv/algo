import sys
input = sys.stdin.readline

N = int(input())
nums = sorted([*map(int, input().split())])
ans = 0
for i in range(N):
    g = nums[i]
    start = 0
    end = N-1
    while start < end:
        r = nums[start] + nums[end]
        if r == g:
            if start == i: start += 1
            elif end == i : end -= 1
            else: 
                ans +=1
                break
        elif r > g:
            end -= 1
        elif r < g:
            start += 1

print(ans)