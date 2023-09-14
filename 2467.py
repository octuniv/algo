import sys
input = sys.stdin.readline

N = int(input())
fluid = [*map(int, input().split())]
left, right = 0, N-1
ans = [-1, N+1]
m_diff = 2000000001
while left < right:
    diff = fluid[right] + fluid[left]
    if m_diff > abs(diff):
        ans = [left, right]
        m_diff = abs(diff)
    if diff > 0:
        right -= 1
    elif diff < 0:
        left += 1
    else:
        break
    
print(f'{fluid[ans[0]]} {fluid[ans[1]]}')