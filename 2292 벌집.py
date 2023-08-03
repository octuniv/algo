import sys
input = sys.stdin.readline

N = int(input())
cnt = 1
end = 1
while N > end:
    end += 6 * cnt
    cnt += 1
    
print(cnt)