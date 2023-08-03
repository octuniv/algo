import math
import sys
input = sys.stdin.readline

N = int(input())
arr = []
sum_num = 0
nums = [0] * 8001
c = N
ran = [500001, -1]
nf, f = [], 0

def round(x):
    if x % 1 >= 0.5: return math.ceil(x)
    else: return math.floor(x)

while c > 0:
    inp = int(input())
    arr.append(inp)
    sum_num += inp
    nums[inp + 4000] += 1
    c -= 1

arr.sort()
print(round(sum_num / N))
print(arr[int(N/2)])
for i in range(len(nums)):
    if nums[i] > 0:
        if ran[0] > i:
            ran[0] = i - 4000
        if ran[1] < i:
            ran[1] = i - 4000
        if nums[i] > f:
            f = nums[i]
            nf = [i - 4000]
        elif nums[i] == f:
            nf.append(i - 4000)
print(nf[0] if len(nf) < 2 else nf[1])
print(ran[1] - ran[0])