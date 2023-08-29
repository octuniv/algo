import sys
input = sys.stdin.readline

max_val = pow(2, 31)
nums = [max_val for _ in range(200002)]
idx = 0
ans = []

N = int(input().rstrip())
for _ in range(N):
    s = int(input().rstrip())
    if s == 0:
        if idx == 0:
            ans.append(0)
        else:
            ans.append(nums[1])
            nums[1], nums[idx] = nums[idx], max_val
            idx -= 1
            a = 1
            while a <= idx:
                hl, hr = 2 * a, 2 * a + 1
                h = hl if nums[hl] < nums[hr] else hr
                if nums[a] > nums[h]:
                    nums[a], nums[h] = nums[h], nums[a]
                    a = h
                else:
                    break
    else:
        idx += 1
        nums[idx] = s
        a = idx
        while a > 1:
            h = a // 2
            if nums[a] < nums[h]:
                nums[a], nums[h] = nums[h], nums[a]
                a = h
            else:
                break
            
for a in ans:
    print(a)