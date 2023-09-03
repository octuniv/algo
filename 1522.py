import sys
input = sys.stdin.readline

strings = [*input().rstrip()]
a = strings.count('a')
len_sts = len(strings)
ans, count = 1000, 0

for idx in range(a - 1):
    if strings[idx] == 'b':
        count += 1

for idx in range(a - 1, len_sts + a - 1):
    if strings[idx % len_sts] == 'b':
        count += 1
    ans = min(ans, count)
    if strings[(idx - a + 1) % len_sts] == 'b':
        count -= 1

print(ans if a != 0 else 0)